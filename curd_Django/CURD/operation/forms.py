# Description: This file contains the forms for the application.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

# -rgister or  create a new user

class RegisterForm(UserCreationForm):
    phone = forms.IntegerField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))

    class Meta:
        model = User
        fields = ["username", 'email',"phone", 'password1', 'password2']


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
