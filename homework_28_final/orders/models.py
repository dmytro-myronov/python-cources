from django.db import models
from customers.models import Customer
from cars.models import Car

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),       # ← Добавили для заказов из Telegram
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='customer_profile',
        null=True, blank=True
    )
    guest_email = models.EmailField(null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  # ← по умолчанию pending

    def __str__(self):
        return f"Order #{self.id} ({self.status})"
