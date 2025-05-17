from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('edit-profile/', views.edit_profile_view, name='edit_profile'),
    path('change-password/', views.change_password_view, name='change_password'),
    path('profile/', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
]