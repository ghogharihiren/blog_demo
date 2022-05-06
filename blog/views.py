import re
from django.shortcuts import redirect, render
from .forms import*
from .models import*
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

def register(request):
    form1=RegisterForm()
    if request.method == "POST":
        form=RegisterForm(request.POST)
        if form.is_valid():    
            form.save()
            messages.success(request,'account creatde by ' + form.cleaned_data['username'])
            return redirect('login')
        else:
            messages.info(request,'enter the valid data')
            return render(request,'register.html',{'form':form1})
    else:
        return render(request,'register.html',{'form':form1})
    
    
def loginpage(request):
    form1=Userlogin()
    if request.method == "POST":
        form=Userlogin(request=request,data=request.POST)
        if form.is_valid():
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return render(request,'login.html',{'form':form1})
        else:
            return render(request,'login.html',{'form':form})    
    form=Userlogin()
    return render(request,'login.html',{'form':form1})   
        
def home(request):
    blog=Post.objects.all()[::-1]
    return render(request,'home.html',{'post':blog})


def logout_user(request):
    logout(request)
    return redirect('login')


def blog(request):
    post=PostForm()
    if request.method == 'POST':
        post1=PostForm(request.POST)
        if post1.is_valid():
            messages.success(request,'you create blog succesfuly')
            p = post1.save(commit=False)
            p.uid = request.user
            p.save()
            return redirect('my-blog')
        return render(request,'blog.html',{'post':post})
    return render(request,'blog.html',{'post':post}) 

def profile(request):
    fm1=Editprofile(instance=request.user)
    if request.user.is_authenticated:
        if request.method == "POST":
            fm=Editprofile(request.POST,instance=request.user)
            if fm.is_valid():
                messages.success(request,'your profile update')
                fm.save()
                return redirect('profile')
            else:
                messages.info(request,'enter valid data for update profile')
                return render(request,'profile.html',{'fm':fm1})
        return render(request,'profile.html',{'fm':fm1})
    else:
        return redirect('login')
    
def my_blog(request):
    post=Post.objects.filter(uid=request.user)[::-1]   
    return render(request,'my-blog.html',{'post':post})


def update_post(request,pk):
    blog=Post.objects.get(id=pk)
    post=PostForm(instance=blog)
    if request.method == 'POST':
        post1=PostForm(request.POST,instance=blog)
        if post1.is_valid():
            post1.save()
            return redirect('my-blog')
        return render(request,'update-post.html',{'post':post})
    return render(request,'update-post.html',{'post':post})

def delete_poat(request,pk):
    blog=Post.objects.get(id=pk)
    blog.delete()
    return redirect('my-blog')

def forgot_password(request):
    password1=PasswordChangeForm(user=request.user)
    if request.method == "POST":
        fm=PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            messages.success(request,'your password change')
            return redirect('profile')
        else:
            messages.info(request,'enter correct password')
            return render(request,'forgot-password.html',{'pass':password1})
    else:
         return render(request,'forgot-password.html',{'pass':password1})
    