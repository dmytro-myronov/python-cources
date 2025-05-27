from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from .filters import CarFilter
from .models import Car
from .permissions import PostRequiresAuthPermission
from .serializers import CarSerializer


class CarViewSet(ModelViewSet):
    """
    A viewset for viewing and editing Car instances.

    - GET: Public access to list and retrieve cars.
    - POST, PUT, PATCH, DELETE: Require authentication.

    Permissions:
        - Only authenticated users can create, update, or delete cars.
        - Everyone can view cars (list/retrieve).

    Authentication:
        - Basic Authentication is used for secured endpoints.
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [PostRequiresAuthPermission]
    queryset: type = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter
