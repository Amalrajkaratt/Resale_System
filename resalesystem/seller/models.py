from django.db import models

# Create your models here.


class SellerRegister(models.Model):
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
    
class Category(models.Model):
    Name=models.CharField(max_length=50)
    def __str__(self):
        return self.Name
    

class Product(models.Model):
    Username=models.ForeignKey(SellerRegister,on_delete=models.CASCADE)
    Product_Name=models.CharField(max_length=50,default='')
    Product_Category=models.ForeignKey(Category,on_delete=models.CASCADE,default='')
    Product_Description=models.TextField(max_length=300)
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
    Product_Price = models.CharField(max_length=15)
    Mobile=models.CharField(max_length=10)
    Email=models.EmailField()
    
    
class Feedbacks(models.Model):
    Name=models.CharField(max_length=20)
    Username=models.ForeignKey(SellerRegister,default=1,on_delete=models.CASCADE)
    Message=models.TextField()
    
class ContactUs(models.Model):
    Contact_Name=models.CharField(max_length=20,default='')
    Contact_Email=models.EmailField(default='')
    Contact_message=(models.CharField(max_length=200,default=''))