from django.db import models
from seller . models import Product
# Create your models here.


class BuyerRegister(models.Model):
    Fullname=models.CharField(max_length=30)
    Username=models.CharField(max_length=50,unique=True)
    Email=models.EmailField()
    Mobile=models.CharField(max_length=10,default='')
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        
    )
    Gender = models.CharField(max_length=6, choices=GENDER_CHOICES,default='Male')
    Age=models.IntegerField()
    Password=models.CharField(max_length=8)
    def __str__(self):
        return self.Username
    
class AddToWishlist(models.Model):
    Buyer=models.ForeignKey(BuyerRegister,on_delete=models.CASCADE)
    Products=models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self) :
        return self.Buyer.Fullname
    
class Feedback(models.Model):
    Name=models.CharField(max_length=20)
    Username=models.ForeignKey(BuyerRegister,default=1,on_delete=models.CASCADE)
    Message=models.TextField()
    def __str__(self) :
        return self.Username
    