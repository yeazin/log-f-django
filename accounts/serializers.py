"""Profile API 
"""
from rest_framework import serializers
from accounts.models import Profile
from accounts.models import User


"""
Profile Register API
"""


class ProfileRegisterAPI(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, style={"input_type": "password"})
    confirm_password = serializers.CharField(
        write_only=True, style={"input_type": "password"}
    )

    class Meta:
        model = Profile
        fields = [
            "username",
            "full_name",
            "password",
            "confirm_password",
        ]

    def create(self, validated_data):
        # getting the username & password data
        username = validated_data.pop("username")
        password = validated_data.pop("password")
        confirm_password = validated_data.pop("confirm_password")

        ## check if the username exits
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("Username Already Exists !!")

        ## check if the password mismatch
        if password != confirm_password:
            raise serializers.ValidationError("Password Mismatch !!")

        ## otherwise save the user and create the profile
        else:
            auth_info = {
                "username": username,
                "password": password,
                "confirm_password": confirm_password,
            }

            user_obj = User(**auth_info)
            user_obj.save()

            ## creating profile data
            profile_obj = Profile.objects.create(user=user_obj, **validated_data)
            profile_obj.save()

            return profile_obj


"""
Profile Update API
"""


class ProfileUpdateAPI(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["full_name", "profile_image"]


"""
Profile View API
"""


class ProfileViewAPI(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Profile
        fields = ["username", "full_name", "profile_image"]


"""
Login Serializer 
"""


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={"input_type": "password"})
