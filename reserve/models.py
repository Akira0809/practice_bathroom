from django.db import models

# Create your models here.
class usertime(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    reserve_time = models.CharField(max_length=10)
    bath_type = models.IntegerField()