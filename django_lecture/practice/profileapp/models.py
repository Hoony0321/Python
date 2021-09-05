from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    image = models.ImageField(upload_to='profiles/', default='profiles/default_profile.png',null=True)
    nickname = models.CharField(max_length=20, null=True, default="NO NICKNAME", unique=True)
    message = models.CharField(max_length=100, null=True, default="NO MESSAGE")

    favorite = JSONField(null=True)
    

