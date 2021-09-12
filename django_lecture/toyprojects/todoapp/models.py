from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True)
    complete = models.BooleanField(default=False)