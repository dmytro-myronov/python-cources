from time import timezone
from django.utils import timezone
from datetime import timedelta
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class User(models.Model):
    telephone_number = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=120)


class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def short_description(self):
        return self.description[:100] + ('...' if len(self.description) > 100 else '')

    def deactivate_if_expired(self):
        if self.created_at <= timezone.now() - timedelta(days=30):
            self.is_active = False
            self.save()



class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    ad = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.ad.title}"

    @staticmethod
    def comments_count_for_ad(ad):
        return Comment.objects.filter(ad=ad).count()
