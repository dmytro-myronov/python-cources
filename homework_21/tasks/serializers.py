from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Task
from datetime import date
from typing import Any, Dict

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the Django built-in User model.

    Serializes the user's id, username, and email.
    """

    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.

    Serializes the task title, description, due_date, and user.
    Includes nested serialization for the user.
    Validates that due_date is not in the past.
    """

    user: UserSerializer = UserSerializer()

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'user']

    def validate_due_date(self, value: date) -> date:
        """
        Ensure the due date is not in the past.

        Args:
            value (date): The input due date.

        Returns:
            date: The validated due date.

        Raises:
            serializers.ValidationError: If the due date is earlier than today.
        """
        if value < timezone.now().date():
            raise serializers.ValidationError("Дата виконання не може бути в минулому")
        return value

    def create(self, validated_data: Dict[str, Any]) -> Task:
        """
        Create and return a new Task instance from validated data.

        Args:
            validated_data (dict): The validated data including nested user info.

        Returns:
            Task: The created Task instance.
        """
        user_data = validated_data.pop('user')
        user = User.objects.get(pk=user_data['id'])
        return Task.objects.create(user=user, **validated_data)
