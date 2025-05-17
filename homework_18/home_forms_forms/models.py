from django.contrib.auth.models import User
from django.db import models
from django.db.models import DateField, OneToOneField, TextField, CharField, ImageField


class UserProfile(models.Model):
    user: OneToOneField = models.OneToOneField(User, on_delete=models.CASCADE)
    bio: TextField = models.TextField(max_length=500, blank=True)
    birth_date: DateField = models.DateField(null=True, blank=True)
    location: CharField = models.CharField(max_length=100, blank=True)
    avatar: ImageField = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username