from django.urls import path

from . import views
from .views import home, about, ContactView, ServiceView

urlpatterns = [
    path('', home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('services/', ServiceView.as_view(), name='services'),
]

