from django.db import models

# Create your models here.

class Account(models.Model):
    uname = models.CharField(max_length=200)
   