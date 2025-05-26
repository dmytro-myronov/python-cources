from django.urls import path
from .views import register_user, update_user

urlpatterns = [
    path('register/', register_user),
    path('update/', update_user),
]
