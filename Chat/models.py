from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    author = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateField(auto_now_add=True, blank=True , null=True)
# Create your models here.
