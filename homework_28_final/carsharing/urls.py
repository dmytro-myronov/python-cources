from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cars.views import CarViewSet
from customers.views import CustomerViewSet
from orders.views import OrderViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', obtain_auth_token),
]
