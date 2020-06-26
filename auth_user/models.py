from django.db import models
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount


class UserProfile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', default=None)
    userAuth = models.OneToOneField(SocialAccount, on_delete=models.CASCADE, related_name='profile', default=None)

