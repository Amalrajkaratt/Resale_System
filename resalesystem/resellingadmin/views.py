from django.shortcuts import render,redirect
from django.contrib import messages
from . models import AdminPage
from . forms import AdminPageForm,AdminSellerUpdateForm,AdminUpdateProductForm,AdminBuyerUpdateForm
from django.contrib.auth import logout as logouts
from seller . models import SellerRegister,Product,Feedbacks
from buyer . models import BuyerRegister,Feedback

# Create your views here.

# admin login
def adminlogin(request):
    if request.method=='POST':
        form=AdminPageForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['UserId']
            password=form.cleaned_data['Password']
        try:
            # checking availablity of the user
            user=AdminPage.objects.get(UserId=email)

            # checking whether the email exists or not
            if not user:
                messages.warning(request,"User does not exist")
                return redirect('/adminlogin')
            
            
            # checking whether the password is correct or not
            elif password!=user.Password:
                messages.warning(request,"Incorrect Password")
                return redirect('/adminlogin')
            
            else:
                messages.warning(request,"Login success")
                return redirect('/adminloginhome/%s' % user.id)
        except:
            messages.warning(request,"Userid or password error")
    else:
        form=AdminPageForm()
    return render(request,'adminlogin.html',{'form':form})
# Admin login END


def adminloginhome(request,id):
    seller=SellerRegister.objects.all()
    buyer=BuyerRegister.objects.all()
    return render(request,'adminloginhome.html',{'seller':seller,'buyer':buyer})

# Seller Details Start
def show_seller(request):
    seller=SellerRegister.objects.all()
    return render(request,'show_seller.html',{'seller':seller})

def adminupdateseller(request,id):
    updateuser=SellerRegister.objects.get(id=id)
    form=AdminSellerUpdateForm(request.POST,instance=updateuser)
    if form.is_valid():
        form.save()
        messages.success(request,"Record updated succesfully")
        return redirect('/show_seller' )
    else:
        form=AdminSellerUpdateForm(instance=updateuser)
    return render(request,'adminupdateseller.html',{'form':form})


def adminseller_delete(request,id):
    User=SellerRegister.objects.get(id=id)
    User.delete()
    messages.success(request,"User Deleted")
    return redirect('/show_seller')


def show_sellerproducts(request):
    product=Product.objects.all()
    return render(request,'show_sellerproducts.html',{'product':product})

def adminupdateproduct(request,id):
    product=Product.objects.get(id=id)
    form=AdminUpdateProductForm(request.POST,instance=product)
    if form.is_valid():
        form.save()
        messages.success(request,"Record updated succesfully")
        return redirect('/show_sellerproducts')
    else:
        form=AdminUpdateProductForm(instance=product)
    return render(request,'adminupdateproduct.html',{'form':form})

def adminsellerproduct_delete(request,id):
    product=Product.objects.get(id=id)
    product.delete()
    messages.success(request,"Product Deleted")
    return redirect('/show_sellerproducts')

# Seller Details End

#Buyer Details Start 
def show_buyer(request):
    buyer=BuyerRegister.objects.all()
    return render(request,'show_buyer.html',{'buyer':buyer})

def adminupdatebuyer(request,id):
    updateuser=BuyerRegister.objects.get(id=id)
    form=AdminBuyerUpdateForm(request.POST,instance=updateuser)
    if form.is_valid():
        form.save()
        messages.success(request,"Record updated succesfully")
        return redirect('/show_buyer')
    else:
        form=AdminBuyerUpdateForm(instance=updateuser)
    return render(request,'adminupdatebuyer.html',{'form':form})

def adminbuyer_delete(request,id):
    User=BuyerRegister.objects.get(id=id)
    User.delete()
    messages.success(request,"User Deleted")
    return redirect('/show_buyer')

# Buyer Details End


def show_feedbacks(request):
    seller=Feedbacks.objects.all()
    buyer_feedbacks=Feedback.objects.all()
    return render(request,'show_feedbacks.html',{'seller':seller,'buyer':buyer_feedbacks})



# ADMIN LOGOUT
def admin_logout(request):
    logouts(request)
    messages.success(request,'Logout Succesful')
    return redirect('/')
# ADMIN LOGOUT

