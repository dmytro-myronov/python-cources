from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    driver_license_number = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
