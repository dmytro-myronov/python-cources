from django.db import models

class Car(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('maintenance', 'Maintenance'),
    ]
    model = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    mileage = models.PositiveIntegerField()
    price = models.FloatField(null=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.model} ({self.license_plate})"
