from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """
    Represents a customer who can rent cars.

    Attributes:
        user (User): A one-to-one relation with Django's built-in User model.
        name (str): Full name of the customer.
        email (str): Unique email address of the customer.
        phone (str): Phone number of the customer.
        driver_license_number (str): Unique driver license number.
    """

    user: User = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    name: str = models.CharField(max_length=100)
    email: str = models.EmailField(unique=True)
    phone: str = models.CharField(max_length=15)
    driver_license_number: str = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name
