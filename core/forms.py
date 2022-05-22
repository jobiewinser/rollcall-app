from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User