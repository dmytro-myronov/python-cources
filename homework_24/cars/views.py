from rest_framework.authentication import BasicAuthentication
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from .models import Car
from .permissions import PostRequiresAuthPermission
from .serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [PostRequiresAuthPermission]
    queryset = Car.objects.all()
    serializer_class = CarSerializer
