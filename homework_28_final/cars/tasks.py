from celery import shared_task
from django.core.mail import send_mail

from cars.models import Car
from customers.models import Customer


@shared_task
def send_rent_car(email: str, car: Car, customer: Customer) -> None:
    """
    Send an email notification when a car is rented.

    Args:
        email (str): The recipient email address.
        car (Car): The Car instance that was rented.
        customer (Customer): The Customer instance who rented the car.

    Returns:
        None
    """
    customer_name: str = customer.name
    customer_email: str = customer.email

    rented_car_message: str = (
        f"Car {car.model} was rented by {customer_name} at {customer_email}"
    )

    send_mail(
        subject=f"Car was rented: {car.model}",
        message=rented_car_message,
        from_email='noreply@carsharing.com',
        recipient_list=[email],
    )
