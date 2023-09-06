from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text','category','tags','image'] 

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['user_profile', 'first_name', 'username', 'email',
                  'gender', 'dob', 'phone_no', 'city', 'state', 'zip_code', 'country']


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['user_profile', 'first_name', 'email', 'gender',
                  'dob', 'phone_no', 'city', 'state', 'zip_code', 'country']           