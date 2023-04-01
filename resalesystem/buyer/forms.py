from django import forms
from . models import BuyerRegister,AddToWishlist,Feedback


class BuyerRegisterForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=BuyerRegister
        fields='__all__'

class BuyerLoginForm(forms.ModelForm):
    class Meta():
        model=BuyerRegister
        fields=('Email','Password')

class BuyerUpdateForm(forms.ModelForm):
    class Meta():
        model=BuyerRegister
        fields=('Fullname','Username','Email','Mobile','Gender','Age')

class BuyerChangePasswordForm(forms.Form):
    OldPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    NewPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    ConfirmNewPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)

class AddToWishlistForm(forms.ModelForm):
    class Meta():
        model=AddToWishlist
        fields='__all__'
        
class FeedbacksForm(forms.ModelForm):
    Username=forms.CharField(required=False)
    class Meta():
        model=Feedback
        fields='__all__'