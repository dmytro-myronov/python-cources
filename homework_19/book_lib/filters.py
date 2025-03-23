import django_filters
from .models import Book


class BookFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(field_name="author", lookup_expr="icontains")
    genres = django_filters.CharFilter(field_name="genres", lookup_expr="icontains")

    class Meta:
        model = Book
        fields: list = ['author', 'genres']