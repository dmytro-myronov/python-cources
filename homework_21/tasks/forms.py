from django import forms
from django.utils import timezone
from datetime import date

class TaskForm(forms.Form):
    """
    A Django form for creating or updating tasks.

    Fields:
        - title: Required short text for the task title.
        - description: Optional detailed text area for task description.
        - due_date: Required date field specifying when the task is due.

    Validations:
        - Ensures the due_date is not in the past.
    """

    title: forms.CharField = forms.CharField(max_length=100)
    description: forms.CharField = forms.CharField(widget=forms.Textarea, required=False)
    due_date: forms.DateField = forms.DateField()

    def clean_due_date(self) -> date:
        """
        Validate that the due date is not in the past.

        Returns:
            date: The validated due date.

        Raises:
            forms.ValidationError: If the due date is earlier than today.
        """
        due_date: date = self.cleaned_data['due_date']
        if due_date < timezone.now().date():
            raise forms.ValidationError("Дата виконання не може бути в минулому")
        return due_date
