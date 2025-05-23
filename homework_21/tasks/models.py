from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Task(models.Model):
    """
    A model representing a task assigned to a user.

    Fields:
        - title: A short title for the task (max 100 characters).
        - description: An optional detailed description of the task.
        - due_date: The date by which the task should be completed.
        - user: The user to whom the task is assigned.
    """

    title: str = models.CharField(max_length=100)
    description: str = models.TextField(blank=True)
    due_date: date = models.DateField()
    user: User = models.ForeignKey(User, on_delete=models.CASCADE)
