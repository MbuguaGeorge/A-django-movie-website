from django import forms
from .models import User_Account
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
  
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email')