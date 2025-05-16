from celery import shared_task
from django.core.mail import send_mail

from cars.models import Car
from customers.models import Customer


@shared_task
def send_rent_car(email,car:Car,customer:Customer):
    customer_name = customer.name
    customer_email = customer.email
    rented_car_message = f"Car {car.model} was rented by {customer_name} at {customer_email}"
    send_mail(
        subject=f"Car was rented {car.model}",
        message=rented_car_message,
        from_email='noreply@carsharing.com',
        recipient_list=[email],
    )
