from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from book_lib.filters import BookFilter
from book_lib.models import Book
from book_lib.serializer import BookSerializer, UserCreateSerializer
from django.contrib.auth.models import User
from rest_framework.request import Request


class StandardResultsSetPagination(PageNumberPagination):
    """
    Custom pagination class to limit the number of results per page.
    """
    page_size: int = 10
    page_size_query_param: str = 'page_size'
    max_page_size: int = 10


class BookViewSet(ModelViewSet):
    """
    API endpoint that allows books to be viewed, filtered, and deleted.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]
    ordering = ['publication_year']

    def destroy(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        """
        Delete a book instance.
        """
        return super().destroy(request, *args, **kwargs)


class UserCreateView(generics.CreateAPIView):
    """
    API endpoint that allows new users to be created.
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]


