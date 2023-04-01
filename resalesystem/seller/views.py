from django.shortcuts import render,redirect
from django.contrib import messages
from . models import SellerRegister,Product,Feedbacks
from . forms import SellerRegisterForm,SellerLoginForm,SellerUpdateForm,SellerChangePasswordForm,ProductForm,UpdateProductForm,FeedbackForm
from django.contrib.auth import logout as logouts
from resalesystem import settings
from django.core.mail  import send_mail


# Create your views here.
def index(request):
    product=Product.objects.all().order_by("-id")
    return render(request,'index.html',{'product':product})


def sellerregister(request):
    if request.method=='POST':
        form=SellerRegisterForm(request.POST)
        if form.is_valid():
            fullname=form.cleaned_data['Fullname']
            username=form.cleaned_data['Username']
            email=form.cleaned_data['Email']
            mobile=form.cleaned_data['Mobile']
            gender=form.cleaned_data['Gender']
            age=form.cleaned_data['Age']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']

            user=SellerRegister.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,'user already exists')
                return redirect('/sellerregister')
            
            elif password!=confirmpassword:
                messages.warning(request,'password mismatch')
                return redirect('/sellerregister')
            else:
                tab=SellerRegister(Fullname=fullname,Username=username,Email=email,Mobile=mobile,Gender=gender,Age=age,Password=password)
                tab.save()
                messages.success(request,'Account created succesfully')
                return redirect('/sellerregister')
    else:
        form=SellerRegisterForm()
    return render(request,'seller_register.html',{'form':form})


def sellerlogin(request):
    if request.method=='POST':
        form=SellerLoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            try:
                user=SellerRegister.objects.get(Email=email)
                if not user:
                    messages.warning(request,'user does not exists')
                    return redirect('/sellerlogin')
                elif password != user.Password:
                    messages.warning(request,'password incorrect')
                    return redirect('/sellerlogin')
                else:
                    messages.success(request,'Logged in As')
                    return redirect('/seller_dashboard/%s' % user.id)
            except:
                messages.warning(request,'email or passsword incorrect')
                return redirect('/sellerlogin')
    else:
        form=SellerLoginForm()
    return render(request,'seller_login.html',{'form':form})

def seller_dashboard(request,id):
    user=SellerRegister.objects.get(id=id)
    return render(request,'seller_dashboard.html',{'user':user})

def seller_update(request,id):
    user=SellerRegister.objects.get(id=id)
    if request.method=='POST':
        form=SellerUpdateForm(request.POST or None,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'Update Succesful')
            return redirect('/seller_dashboard/%s' % user.id)
    else:
        form=SellerUpdateForm(instance=user)
    return render(request,'seller_update.html',{'form':form,'user':user})


def seller_changepassword(request,id):
    user=SellerRegister.objects.get(id=id)
    if request.method=='POST':
        form=SellerChangePasswordForm(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data['OldPassword']
            newpassword=form.cleaned_data['NewPassword']
            confirmnewpassword=form.cleaned_data['ConfirmNewPassword']
            if oldpassword!=user.Password:
                messages.warning(request,'Old Password incorrect')
                return redirect('/seller_changepassword/%s' % user.id)
            elif oldpassword==newpassword:
                messages.warning(request,'New Password Matches The Old Password')
                return redirect('/seller_changepassword/%s' % user.id)
            elif newpassword!=confirmnewpassword:
                messages.warning(request,'New Password And Confirm Password Does Not Match')
                return redirect('/seller_changepassword/%s' % user.id)
            else:
                user.Password=newpassword
                user.save()
                messages.success(request,'Password Change Succesful')
                return redirect('/seller_dashboard/%s' % user.id)
    else:
        form=SellerChangePasswordForm()
    return render(request,'seller_changepassword.html',{'form':form,'user':user})


def seller_logout(request):
    logouts(request)
    messages.success(request,'Logout Succesful')
    return redirect('/')

def seller_delete(request,id):
    User=SellerRegister.objects.get(id=id)
    User.delete()
    messages.success(request,"User Deleted")
    return redirect('/')

def add_product(request,id):
    user=SellerRegister.objects.get(id=id)
    if request.method=='POST':
        form=ProductForm(request.POST or None,request.FILES or None,instance=user)
        if form.is_valid():
            usr=SellerRegister.objects.get(id=id)
            productname=form.cleaned_data['Product_Name']
            productcat=form.cleaned_data['Product_Category']
            productdes=form.cleaned_data['Product_Description']
            photo=form.cleaned_data['Photo']
            productprice=form.cleaned_data['Product_Price']
            email=form.cleaned_data['Email']
            mobile=form.cleaned_data['Mobile']
           
            
            tab=Product(Product_Name=productname,Product_Category=productcat,Product_Description=productdes,Photo=photo,Product_Price=productprice,Username=usr,Mobile=mobile,Email=email)
            tab.save()         
            messages.success(request,'Product Added Succesfully')
            return redirect('/add_product/%s' % user.id )
    else:
        form=ProductForm(instance=user)
    return render(request,'add_product.html',{'form':form,'user':user})

def show_listedproduct(request,id):
    user=SellerRegister.objects.get(id=id)
    product=Product.objects.filter(Username=id)
    return render(request,'listed_product.html',{'product':product,'user':user})

def seller_productupdate(request,id,pid):
    user=SellerRegister.objects.get(id=id)
    product=Product.objects.get(id=pid)
    form=UpdateProductForm(request.POST,request.FILES,instance=product)
    if form.is_valid():
        form.save()
        messages.success(request,"Record updated succesfully")
        return redirect('/show_listedproduct/%s' % user.id  )
    else:
        form=UpdateProductForm(instance=product)
    return render(request,'seller_productupdate.html',{'form':form})

def seller_productdelete(request,uid,pid):
    user=SellerRegister.objects.get(id=uid)
    
    product=Product.objects.get(id=pid)
    product.delete()
    messages.success(request,"Product Deleted")
    return redirect('/show_listedproduct/%s' % user.id)

def seller_showprofile(request,id):
    user=SellerRegister.objects.get(id=id)
    return render(request,'showprofile.html',{'user':user})

def seller_showname(request,id):
    user=SellerRegister.objects.get(id=id)
    return render(request,'seller_dashboard_base.html',{'users':user})



def feedback(request,id):
    users=SellerRegister.objects.get(id=id)
    if request.method=='POST':
        form=FeedbackForm(request.POST or None,instance=users)
        if form.is_valid():
            usr=SellerRegister.objects.get(id=id)
            name=form.cleaned_data['Name']
            message=form.cleaned_data['Message']

            tab=Feedbacks(Name=name,Username=usr,Message=message)
            tab.save()
            messages.success(request,'Sent Successfully')
            return redirect('/seller_dashboard/%s' % users.id)
    else:
        form=FeedbackForm(instance=users)
    return render(request,'feedback.html',{'form':form})


def mail(request):
    if request.method=="POST":
        cname=request.POST.get('contact_name')
        cemail=request.POST.get('contact_email')
        cmessage=request.POST.get('contact_message')
        toemail="reseliitagain244@gmail.com"
        res = send_mail(cname,cmessage,settings.EMAIL_HOST_USER,[toemail],fail_silently=False)
        if(res == 1):
             messages.success(request,' sent successfull')
        else:
             messages.warning(request,' couldnot sent')
        return redirect('/')
    else:
        return render(request,'index.html') 