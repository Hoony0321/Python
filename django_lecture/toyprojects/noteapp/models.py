from django.db import models

# Create your models here.

class Note(models.Model):

    title = models.CharField(max_length=30, null=False);
    content = models.TextField(null=True); #TextField는 max_length가 없을 때 사용!
    createDate = models.DateField(auto_now_add=True);
    modifyDate = models.DateField(auto_now=True);
