from django.db import models


class Post(models.Model):
    """
    Модель поста с заголовком, содержимым и датой создания.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """
        Возвращает строковое представление поста с заголовком и ID.
        """
        return f"{self.title} (ID: {self.id})"
