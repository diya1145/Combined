from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text','category','tags','image'] 

class RegistrationForm1(forms.ModelForm):
        
    class Meta:
        model = RegistrationForm
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class Update(forms.ModelForm):

    class Meta:
        model = update
        fields = ['username', 'email', 'password']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']

