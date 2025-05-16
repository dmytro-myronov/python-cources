from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_registration_email(email):
    send_mail(
        subject='Welcome',
        message='thanks for registering',
        from_email='noreply@carsharing.com',
        recipient_list=[email],
    )
