from django import forms
from . models import AdminPage
from seller . models import SellerRegister,Product
from buyer . models import BuyerRegister


# Admin page
class AdminPageForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=15)
    class Meta():
        model=AdminPage
        fields=('UserId','Password')
        
class AdminSellerUpdateForm(forms.ModelForm):
    class Meta():
         model=SellerRegister
         fields='__all__'
         
class AdminBuyerUpdateForm(forms.ModelForm):
    class Meta():
         model=BuyerRegister
         fields='__all__'
         
class AdminUpdateProductForm(forms.ModelForm):
    class Meta():
        model=Product
        fields='__all__'