from django import forms
from . models import SellerRegister,Product,Feedbacks

# Seller
class SellerRegisterForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=SellerRegister
        fields='__all__'
        
class SellerLoginForm(forms.ModelForm):
    class Meta():
        model=SellerRegister
        fields=('Email','Password')

class SellerUpdateForm(forms.ModelForm):
    class Meta():
        model=SellerRegister
        fields=('Fullname','Username','Email','Mobile','Gender','Age')

class SellerChangePasswordForm(forms.Form):
    OldPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    NewPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    ConfirmNewPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)

class ProductForm(forms.ModelForm):
    Username=forms.CharField(required=False)
    class Meta():
        model=Product
        fields='__all__'

class UpdateProductForm(forms.ModelForm):
    class Meta():
        model=Product        
        fields=('Product_Name','Product_Category','Product_Description','Photo','Product_Price')
        
class FeedbackForm(forms.ModelForm):
    Username=forms.CharField(required=False)
    class Meta():
        model=Feedbacks
        fields='__all__'
