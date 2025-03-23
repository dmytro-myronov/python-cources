from django.apps import AppConfig


class BookLibConfig(AppConfig):
    default_auto_field: str = 'django.db.models.BigAutoField'
    name: str = 'book_lib'
