from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  # Built-in form class, with default fields username, password1, password2

class UserRegistrationForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
