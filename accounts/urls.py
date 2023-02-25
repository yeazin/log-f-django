"""
Profile URLs 

"""

from django.urls import path
from accounts.views import ProfileRegister, ProfileUpdate, ProfileList


urlpatterns = [
    path("", ProfileList.as_view()),
    path("register/", ProfileRegister.as_view()),
    path("<int:pk>/", ProfileUpdate.as_view()),
]
