# company/urls.py
from django.urls import path
from .views import notify_company
from .views import index

urlpatterns = [
    path('notify/<int:company_id>/', notify_company),
    path('index/', index),

]
