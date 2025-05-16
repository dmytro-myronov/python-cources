from celery import shared_task
from django.core.mail import send_mail
import logging

from customers.models import Customer


@shared_task
def send_registration_email(email):
    send_mail(
        subject='Welcome',
        message='thanks for registering',
        from_email='noreply@carsharing.com',
        recipient_list=[email],
    )

@shared_task
def send_promo_email(user_id):
    user = Customer.objects.get(id=user_id)
    send_mail(
        'Discover Our Features',
        'Check out the awesome features of our service!',
        'from@example.com',
        [user.email],
        fail_silently=False,
    )


def log_user_count():
    count = Customer.objects.count()
    logging.info(f"Total users in DB: {count}")