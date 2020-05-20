from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    
