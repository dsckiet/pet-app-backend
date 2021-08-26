from django.db import models
from Owner.models import UserInfo

class PetInfo(models.Model):
    name = models.CharField(max_length=200, default="NULL")
    gender = models.CharField(max_length=200, default="NULL")
    description = models.CharField(max_length=200, default="NULL")
    category = models.CharField(max_length=200, default="NULL")
    breed = models.CharField(max_length=200, default="NULL")
    profile_pet = models.URLField(null=True)
    owner = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    
class CategoryInfo(models.Model):
    category = models.CharField(max_length=200, default="NULL")

class BreedInfo(models.Model):
    breed = models.CharField(max_length=200, default="NULL" )
    category = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
# Create your models here.
