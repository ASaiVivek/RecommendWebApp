from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass

class Music(models.Model):
    title = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    link = models.CharField(max_length=1000,default=None,blank=True,null=True)
    logo = models.CharField(max_length=1000,default=None,blank=True,null=True)
    artist = models.CharField(max_length=30)

