from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from base.models import TimeStampMixin


class CustomUserManager(BaseUserManager):
    """custom user email where email is unique.
    We can also pass Full name , email and password here"""

    def create_user(self, email, password, **extra_fields):
        """Create and save a User given email and password"""
        if not email:
            raise ValueError("The Email is must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and save Super user with given email address"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Supperuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Supperuser must have is_superuser=True")

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, blank=True, unique=True, null=True)
    email = models.EmailField("email_address", unique=True, null=True, blank=True)

    password = models.CharField(max_length=1500, null=True)
    confirm_password = models.CharField(max_length=1500, null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.username)

    class Meta:
        indexes = [models.Index(fields=["id", "username"])]


"""
Profile models 
"""


class Profile(TimeStampMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, null=True, blank=True)
    profile_image = models.ImageField(
        upload_to="media/profile_images/", null=True, blank=False
    )

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "Profile"
