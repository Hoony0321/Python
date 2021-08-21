from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    #OneToOneField = ForiegnKey라고 생각하면 됨. 
    # 즉, 아래 구문은 이 모델(객체)는 user라는 ForiegnKey를 가지고 
    # profile이라는 이름으로 이 모델에 접근 할 수 있다고 생각하면 됨.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=30, null=True)
