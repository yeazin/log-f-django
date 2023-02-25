"""
Profile Views 
"""

from accounts.models import Profile, User
from accounts.serializers import (
    ProfileRegisterAPI,
    ProfileUpdateAPI,
    ProfileViewAPI,
    LoginSerializer,
)

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, status, serializers
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser


"""
Profile Register API view 
"""


class ProfileRegister(generics.CreateAPIView):
    queryset = Profile.objects.filter(is_active=True)
    serializer_class = ProfileRegisterAPI
    permission_classes = ()


"""
Profiel Update View 
"""


class ProfileUpdate(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.filter(is_active=True)
    serializer_class = ProfileUpdateAPI
    parser_classes = [MultiPartParser, FormParser]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        if the user has image and no need to update then
        the image will be last one
        otherwise the image will be updated by given image
        """
        instance = self.get_object()

        if request.user.id != instance.id:
            raise serializers.ValidationError("You don`t have permission to edit")

        if not request.data.get("profile_image", None):
            data = request.data.copy()
            data.pop("profile_image", None)
            serializer = self.get_serializer(
                instance,
                data=data,
                partial=True,
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()

        else:
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response(serializer.data)


"""
Profile List view 
"""


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.filter(is_active=True)
    serializer_class = ProfileViewAPI
    permission_classes = ()


"""
Login view for API Authentication 
"""


class APILoginView(generics.GenericAPIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        ## checking if ther user exists
        ## user can input username
        match_user = User.objects.filter(username=data["username"])
        if match_user.exists():
            user = authenticate(
                username=match_user.first().username, password=data["password"]
            )
            if not user:
                raise serializers.ValidationError({"Error": "Password Mismatch"})
        else:
            raise serializers.ValidationError({"Error": "User doesn`t exists"})

        # generate token
        refresh = RefreshToken.for_user(user)

        return Response(
            {"access_token": str(refresh.access_token), "refresh_token": str(refresh)},
            status=status.HTTP_200_OK,
        )
