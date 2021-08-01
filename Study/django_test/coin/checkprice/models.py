from django.db import models

# Create your models here.
class Currency(models.Model):
    name = models.CharField(max_length=200, default="currency");
    price = models.FloatField(default=0.0);
    change_rate = models.FloatField(default=0.0);
    volume = models.FloatField(default=0.0);
