from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField, DateTimeField, ForeignKey


# Create your models here.
class Book(models.Model):
    """
    Represents a book with details such as title, author, genre, publication year, and metadata.

    This model holds information about books for an application. Used to store
    and retrieve book records. It also specifies metadata for default ordering.

    :ivar title: The title of the book.
    :type title: str
    :ivar author: The author of the book.
    :type author: str
    :ivar genre: The genre of the book.
    :type genre: str
    :ivar publication_year: The publication year of the book.
    :type publication_year: int
    :ivar created_at: The date and time of the record creation.
    :type created_at: datetime.datetime
    :ivar user: The user associated with the book. References a user instance.
    :type user: User
    """
    title: CharField = models.CharField(max_length=255)
    author: CharField = models.CharField(max_length=255)
    genre: CharField = models.CharField(max_length=100)
    publication_year: CharField = models.PositiveIntegerField()
    created_at: DateTimeField = models.DateTimeField(auto_now_add=True)
    user: ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering: list = ['publication_year', 'title']

    def __str__(self) -> str:
        return self.title
