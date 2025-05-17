from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm as DjangoPasswordChangeForm
from django.core.exceptions import ValidationError
from .models import UserProfile


class RegistrationForm(forms.ModelForm):
    password: forms.CharField = forms.CharField(widget=forms.PasswordInput)
    confirm_password: forms.CharField = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self) -> dict:
        cleaned_data: dict = super().clean()
        password: str = cleaned_data.get("password")
        confirm_password: str = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Passwords do not match")

        return cleaned_data

    def clean_email(self) -> str:
        email: str = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'birth_date', 'location', 'avatar']

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if avatar and avatar.size > 2 * 1024 * 1024:
            raise ValidationError("Avatar file size must be under 2MB")
        return avatar


class CustomPasswordChangeForm(DjangoPasswordChangeForm):
    def clean_new_password2(self) -> str:
        new_password1 = self.cleaned_data.get('new_password1')
        old_password = self.cleaned_data.get('old_password')
        if new_password1 == old_password:
            raise ValidationError("New password must be different from the current password")
        return new_password1