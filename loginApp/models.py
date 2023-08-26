from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class User_Profile(models.Model):
    username = models.CharField(max_length=100)
    name =  models.CharField(max_length= 100)
    birthday = models.DateField()
    
    def sace(self,*args,**kwargs):
        super().save(*args,**kwargs)