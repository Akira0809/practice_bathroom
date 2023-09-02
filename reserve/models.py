from django.db import models

# Create your models here.
class usertime(models.Model):
    username = models.CharField(max_length=100)
    reserve_time = models.IntegerField()
    bath_type = models.IntegerField()

class num_people(models.Model):
    num_people = models.JSONField()