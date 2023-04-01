from django.shortcuts import render,redirect
from django.contrib import messages
from . models import BuyerRegister,AddToWishlist,Feedback
from . forms import BuyerRegisterForm,BuyerLoginForm,BuyerUpdateForm,BuyerChangePasswordForm,AddToWishlistForm,FeedbacksForm
from django.contrib.auth import logout as logouts
from seller.models import Product,Category

# Create your views here.



def buyer_register(request):
    if request.method=='POST':
        form=BuyerRegisterForm(request.POST)
        if form.is_valid():
            fullname=form.cleaned_data['Fullname']
            username=form.cleaned_data['Username']
            email=form.cleaned_data['Email']
            mobile=form.cleaned_data['Mobile']
            gender=form.cleaned_data['Gender']
            age=form.cleaned_data['Age']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']

            user=BuyerRegister.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,'user already exists')
                return redirect('/buyer_register')
            
            elif password!=confirmpassword:
                messages.warning(request,'password mismatch')
                return redirect('/buyer_register')
            else:
                tab=BuyerRegister(Fullname=fullname,Username=username,Email=email,Mobile=mobile,Gender=gender,Age=age,Password=password)
                tab.save()
                messages.success(request,'Account created succesfully')
                return redirect('/buyer_register')
    else:
        form=BuyerRegisterForm()
    return render(request,'buyer_register.html',{'form':form})

def buyer_login(request):
    if request.method=='POST':
        form=BuyerLoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            try:
                user=BuyerRegister.objects.get(Email=email)
                if not user:
                    messages.warning(request,'user does not exists')
                    return redirect('/buyer_login')
                elif password != user.Password:
                    messages.warning(request,'password incorrect')
                    return redirect('/buyer_login')
                else:
                    messages.success(request,'Logged in as')
                    return redirect('/buyer_dashboard/%s' % user.id)
            except:
                messages.warning(request,'email or passsword incorrect')
                return redirect('/buyer_login')
    else:
        form=BuyerLoginForm()
    return render(request,'buyer_login.html',{'form':form})



def buyer_dashboard(request,id):
    user=BuyerRegister.objects.get(id=id)
    category=Category.objects.all()
    pro=Product.objects.all()
    return render(request,'buyer_dashboard.html',{'user':user,'category':category,'pro':pro})
    

def show_all_products(request,id):
    user=BuyerRegister.objects.get(id=id)
    pro=Product.objects.all()
    category=Category.objects.all()
    return render(request,'show_all_products.html',{'pro':pro,'category':category,'user':user})



def buyer_update(request,id):
    user=BuyerRegister.objects.get(id=id)
    if request.method=='POST':
        form=BuyerUpdateForm(request.POST or None,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'Update Succesful')
            return redirect('/show_profile/%s' % user.id)
    else:
        form=BuyerUpdateForm(instance=user)
    return render(request,'buyer_update.html',{'form':form,'user':user})


def buyer_changepassword(request,id):
    user=BuyerRegister.objects.get(id=id)
    if request.method=='POST':
        form=BuyerChangePasswordForm(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data['OldPassword']
            newpassword=form.cleaned_data['NewPassword']
            confirmnewpassword=form.cleaned_data['ConfirmNewPassword']
            if oldpassword!=user.Password:
                messages.warning(request,'Old Password incorrect')
                return redirect('/buyer_changepassword/%s' % user.id)
            elif oldpassword==newpassword:
                messages.warning(request,'New Password Matches The Old Password')
                return redirect('/buyer_changepassword/%s' % user.id)
            elif newpassword!=confirmnewpassword:
                messages.warning(request,'New Password And Confirm Password Does Not Match')
                return redirect('/buyer_changepassword/%s' % user.id)
            else:
                user.Password=newpassword
                user.save()
                messages.success(request,'Password Change Succesful')
                return redirect('/show_profile/%s' % user.id)
    else:
        form=BuyerChangePasswordForm()
    return render(request,'Buyer_changepassword.html',{'form':form,'user':user})

def buyer_logout(request):
    logouts(request)
    messages.success(request,'Logout Succesful')
    return redirect('/')

def buyer_delete(request,id):
    User=BuyerRegister.objects.get(id=id)
    User.delete()
    messages.success(request,"User Deleted")
    return redirect('/')
   
    

def show_profile(request,id):
    user=BuyerRegister.objects.get(id=id)
    return render(request,'show_profile.html',{'user':user})





def readcategory(request,id,uid):
    user=BuyerRegister.objects.get(id=uid)
    category=Category.objects.all()
    cats=Category.objects.get(id=id)
    pro=Product.objects.filter(Product_Category=cats)
    return render(request,'readcategory.html',{'cats':cats,'pro':pro,'category':category,'user':user})



def show_productdetail(request,userid,proid):
    user=BuyerRegister.objects.get(id=userid)
    pro=Product.objects.get(id=proid)
    
    wishlist=AddToWishlist.objects.filter(Buyer=user)
    cart=[]
    
    for f in wishlist:
        cart.append(f.id)
    
    context={
        'user':user,
        'pro':pro,
        'cart':cart,
    }
    
    return render(request,'show_productdetail.html',context)



def add_to_wishlist(request,uid,pid):
    user=BuyerRegister.objects.get(id=uid)
    pro=Product.objects.get(id=pid)
    
    try:
        data=AddToWishlist.objects.get(Buyer=user,Products=pro)
        if data:
            data.delete()
            return redirect('/show_productdetail/%s/%s' % (user.id,pro.id))
    except:
        data=AddToWishlist(Buyer=user,Products=pro)
        data.save()
        messages.success(request,'Added to wishlist')
        return redirect('/show_productdetail/%s/%s' % (user.id,pro.id))
    
def wishlist(request,id):
    user=BuyerRegister.objects.get(id=id)
    pro=AddToWishlist.objects.filter(Buyer=user)
    return render(request,'wishlist.html',{'pro':pro,'user':user})


def b_feedback(request,id):
    user=BuyerRegister.objects.get(id=id)
    if request.method=='POST':
        form=FeedbacksForm(request.POST or None,instance=user)
        if form.is_valid():
            usr=BuyerRegister.objects.get(id=id)
            name=form.cleaned_data['Name']
            message=form.cleaned_data['Message']

            tab=Feedback(Name=name,Username=usr,Message=message)
            tab.save()
            messages.success(request,'Sent Successfully')
            return redirect('/buyer_dashboard/%s' % user.id)
    else:
        form=FeedbacksForm(instance=user)
    return render(request,'b_feedback.html',{'form':form,'user':user})