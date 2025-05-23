import uuid
from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date, timedelta
from tasks.serializers import TaskSerializer
from tasks.forms import TaskForm

class TaskSerializerTest(TestCase):
    """
    Unit tests for the TaskSerializer and TaskForm functionalities.
    """

    def setUp(self) -> None:
        """
        Set up a test user for use in all tests.
        """
        self.user: User = User.objects.create_user(
            username='user2',
            password='pass',
            email='u@example.com'
        )

    def test_form_valid_data(self) -> None:
        """
        Test TaskForm with valid data is considered valid.
        """
        form = TaskForm(data={
            'title': 'Test Task',
            'description': 'Some description',
            'due_date': (date.today() + timedelta(days=1)).isoformat(),
        })
        self.assertTrue(form.is_valid())

    def test_valid_serializer(self) -> None:
        """
        Test TaskSerializer with valid data passes validation.
        """
        data = {
            "title": "Test Task",
            "description": "Some description",
            "due_date": (date.today() + timedelta(days=1)).isoformat(),
            "user": {
                "id": self.user.id,
                "username": f"{self.user.username}{uuid.uuid4()}",
                "email": self.user.email
            }
        }
        serializer = TaskSerializer(data=data)
        valid: bool = serializer.is_valid()
        print(serializer.errors)  # Debugging output for development
        self.assertTrue(valid)
        self.assertTrue(serializer.is_valid())

    def test_due_date_in_past(self) -> None:
        """
        Test TaskSerializer validation fails if due_date is in the past.
        """
        data = {
            "title": "Test Task",
            "description": "Some description",
            "due_date": (date.today() - timedelta(days=1)).isoformat(),
            "user": {
                "id": self.user.id,
                "username": self.user.username,
                "email": self.user.email
            }
        }
        serializer = TaskSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("due_date", serializer.errors)
