from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from .models import Customer

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Customer
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@gmail.com'):
            raise ValidationError("Только Gmail адреса разрешены.")
        return email

class UserLoginForm(AuthenticationForm):
    pass
