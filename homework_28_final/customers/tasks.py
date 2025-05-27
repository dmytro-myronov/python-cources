from typing import Optional
from celery import shared_task
from django.core.mail import send_mail
import logging

from customers.models import Customer


@shared_task
def send_registration_email(email: str) -> None:
    """
    Send a registration welcome email to the given email address.

    Args:
        email (str): Recipient email address.
    """
    send_mail(
        subject='Welcome',
        message='Thanks for registering',
        from_email='noreply@carsharing.com',
        recipient_list=[email],
    )


@shared_task
def send_promo_email(user_id: int) -> None:
    """
    Send a promotional email to the customer identified by user_id.

    Args:
        user_id (int): The ID of the Customer to send the email to.
    """
    user: Optional[Customer] = Customer.objects.filter(id=user_id).first()
    if not user:
        logging.error(f"Customer with id {user_id} not found for promo email.")
        return

    send_mail(
        subject='Discover Our Features',
        message='Check out the awesome features of our service!',
        from_email='from@example.com',
        recipient_list=[user.email],
        fail_silently=False,
    )


def log_user_count() -> None:
    """
    Log the total number of users in the database.
    """
    count = Customer.objects.count()
    logging.info(f"Total users in DB: {count}")
