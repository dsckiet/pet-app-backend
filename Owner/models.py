from django.db import models
from django.db.models.base import Model

class UserInfo(models.Model):
    username = models.CharField(max_length=200, default="NULL" , unique= True )
    name = models.CharField(max_length=200, default="NULL")
    email = models.EmailField(max_length=200, default="NULL" , unique= True)
    password = models.CharField(max_length=200, default="NULL")

    
# Create your models here.
