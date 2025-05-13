from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Advertisement

@receiver(post_save, sender=Advertisement)
def notify_user_on_new_ad(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Ваше оголошення створено',
            f'Ви щойно створили оголошення: {instance.title}',
            'noreply@board.com',
            [instance.user.email],
            fail_silently=True,
        )

@receiver(post_save, sender=Advertisement)
def deactivate_old_ads(sender, instance, **kwargs):
    instance.deactivate_if_expired()
