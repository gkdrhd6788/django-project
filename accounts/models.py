from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name = 'followers' )