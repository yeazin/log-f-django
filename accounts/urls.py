"""
Profile URLs 

"""

from django.urls import path
from accounts.views import (
    ProfileRegister,
    ProfileUpdate,
    ProfileList,
    APILoginView,
    APILogoutView,
)


urlpatterns = [
    path("login/", APILoginView.as_view()),
    path("logout/", APILogoutView.as_view()),
    path("", ProfileList.as_view()),
    path("register/", ProfileRegister.as_view()),
    path("<int:pk>/", ProfileUpdate.as_view()),
]
