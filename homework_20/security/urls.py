from django.urls import path

from security import views

urlpatterns = [
    path('customer/register/', views.register_view,name='register'),
    path('customer/login/', views.login_view,name='login'),
    path('customer/profile/', views.profile_view,name='profile'),
    path('customer/logout/', views.logout_view,name='profile'),
]
