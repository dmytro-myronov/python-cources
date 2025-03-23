from rest_framework import serializers
from rest_framework.serializers import ALL_FIELDS
from django.contrib.auth.models import User
from book_lib.models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    """
    class Meta:
        model = Book
        fields = ALL_FIELDS

class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a new user.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data: dict) -> User:
        """
        Create and return a new user instance.
        """
        return User.objects.create_user(**validated_data)