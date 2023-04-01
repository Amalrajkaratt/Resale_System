from django.db import models
# Create your models here.
# Admin login model
class AdminPage(models.Model):
    UserId=models.CharField(max_length=15)
    Password=models.CharField(max_length=15)
    
    
