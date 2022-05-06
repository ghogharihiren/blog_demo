
from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


class RegisterForm(UserCreationForm):
    password2=forms.CharField(label='Confirm Password' ,widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['first_name','last_name','username','email']
        
class Userlogin(AuthenticationForm):
    username=forms.CharField(label='Username')
    password=forms.CharField(label='Password',widget=forms.PasswordInput())
    
class Editprofile(UserChangeForm):
    class Meta:
        model=User
        fields= ['username','first_name','last_name','email']   

    
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','content']