from django.db import models
import datetime

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    def __str__(self):
        return self.email
  
class Post(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    content=models.TextField(max_length=1000)
    date=models.DateField(default=datetime.date.today)
      
    def __str__(self):
        return self.title