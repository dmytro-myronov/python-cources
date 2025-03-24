import django_filters
from django_filters import CharFilter

from .models import Book


class BookFilter(django_filters.FilterSet):
    """
    Filter class for Book model.
    Allows filtering by author and genres using case-insensitive search.
    """
    author: CharFilter = django_filters.CharFilter(field_name="author", lookup_expr="icontains")
    genres: CharFilter = django_filters.CharFilter(field_name="genres", lookup_expr="icontains")

    class Meta:
        model: type[Book] = Book
        fields: list[str] = ["author", "genres"]
