from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserRevised(User):
    nickname = models.CharField(max_length=20, null=True)

class Book(models.Model):
    name = models.CharField(max_length=20, null=False)
    author = models.CharField(max_length=20, null=True)
    price = models.IntegerField(default=0)
    published_date = models.DateField(null=True)

    
    