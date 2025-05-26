from django.urls import path

from . import views
from .views import home, about, ContactView, ServiceView

urlpatterns = [
    path('', home, name='home'),
    path('start_chat/', views.about, name='about'),

]
