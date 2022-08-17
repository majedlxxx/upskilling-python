from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class Account(AbstractBaseUser):
    username = models.CharField(max_length=200, unique=True)
    USERNAME_FIELD = 'username'
    