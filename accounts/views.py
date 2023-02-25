"""
Profile Views 
"""

from accounts.models import Profile
from accounts.serializers import ProfileRegisterAPI, ProfileUpdateAPI, ProfileViewAPI

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser


"""
Profile Register API view 
"""


class ProfileRegister(generics.CreateAPIView):
    queryset = Profile.objects.filter(is_active=True)
    serializer_class = ProfileRegisterAPI


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
