from django.db import models

class UserInfo(models.Model):
    username = models.CharField(max_length=200, default="NULL" , unique= True )
    name = models.CharField(max_length=200, default="NULL")
    email = models.EmailField(max_length=200, default="NULL" , unique= True)
    password = models.CharField(max_length=200, default="NULL")

class PetInfo(models.Model):
    name = models.CharField(max_length=200, default="NULL")
    gender = models.CharField(max_length=200, default="NULL")
    description = models.CharField(max_length=200, default="NULL")
    category = models.CharField(max_length=200, default="NULL")
    breed = models.CharField(max_length=200, default="NULL")
    profile_pet = models.URLField(null=True)
    owner = models.ForeignKey(UserInfo, on_delete=models.CASCADE)

    
    
# Create your models here.
