from datetime import timedelta
from django.db import models
from django.utils import timezone


class Category(models.Model):
    """
    Категория, к которой может принадлежать объявление.
    """
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        """
        Возвращает строковое представление категории.
        """
        return self.name


class User(models.Model):
    """
    Пользователь, создающий объявления и комментарии.
    """
    telephone_number = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=120)

    def __str__(self) -> str:
        """
        Возвращает строковое представление пользователя.
        """
        return self.telephone_number


class Advertisement(models.Model):
    """
    Объявление, созданное пользователем.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """
        Возвращает строковое представление объявления.
        """
        return self.title

    def short_description(self) -> str:
        """
        Возвращает сокращённое описание (до 100 символов).
        """
        return self.description[:100] + ('...' if len(self.description) > 100 else '')

    def deactivate_if_expired(self) -> None:
        """
        Деактивирует объявление, если оно создано более 30 дней назад.
        """
        if self.created_at <= timezone.now() - timedelta(days=30):
            self.is_active = False
            self.save()


class Comment(models.Model):
    """
    Комментарий к объявлению от пользователя.
    """
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    ad = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """
        Возвращает строковое представление комментария.
        """
        return f"Comment by {self.user.telephone_number} on {self.ad.title}"

    @staticmethod
    def comments_count_for_ad(ad: Advertisement) -> int:
        """
        Возвращает количество комментариев для конкретного объявления.

        Args:
            ad: Объявление, для которого считаются комментарии.

        Returns:
            int: Количество комментариев.
        """
        return Comment.objects.filter(ad=ad).count()
