# tests/test_forms_functional.py
import pytest
from datetime import date, timedelta
from tasks.forms import TaskForm

def test_form_valid_data() -> None:
    """
    Test that the form is valid when all required fields are correctly filled.
    """
    form = TaskForm(data={
        'title': 'Test Task',
        'description': 'Desc',
        'due_date': (date.today() + timedelta(days=1)).isoformat(),
    })
    assert form.is_valid()

def test_form_missing_required_fields() -> None:
    """
    Test that the form is invalid when required fields are missing.
    """
    form = TaskForm(data={})
    assert not form.is_valid()
    assert 'title' in form.errors
    assert 'due_date' in form.errors

def test_due_date_in_past() -> None:
    """
    Test that the form is invalid if the due date is in the past.
    """
    form = TaskForm(data={
        'title': 'Task',
        'due_date': (date.today() - timedelta(days=1)).isoformat()
    })
    assert not form.is_valid()
    assert 'due_date' in form.errors
    assert form.errors['due_date'][0] == 'Дата виконання не може бути в минулому'
