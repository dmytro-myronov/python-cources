from typing import Any

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Advertisement


@receiver(post_save, sender=Advertisement)
def notify_user_on_new_ad(
    sender: type[Advertisement],
    instance: Advertisement,
    created: bool,
    **kwargs: Any
) -> None:
    """
    Отправляет письмо пользователю при создании нового объявления.

    Args:
        sender: Класс модели, отправивший сигнал.
        instance: Экземпляр модели Advertisement.
        created: Флаг, указывающий, что объект был создан (а не обновлён).
        **kwargs: Дополнительные аргументы сигнала.
    """
    if created:
        send_mail(
            'Ваше оголошення створено',
            f'Ви щойно створили оголошення: {instance.title}',
            'noreply@board.com',
            [instance.user.email],
            fail_silently=True,
        )


@receiver(post_save, sender=Advertisement)
def deactivate_old_ads(
    sender: type[Advertisement],
    instance: Advertisement,
    **kwargs: Any
) -> None:
    """
    Деактивирует объявление, если оно старше 30 дней.

    Args:
        sender: Класс модели, отправивший сигнал.
        instance: Экземпляр модели Advertisement.
        **kwargs: Дополнительные аргументы сигнала.
    """
    instance.deactivate_if_expired()
