import django_filters
from .models import Car

class CarFilter(django_filters.FilterSet):
    model = django_filters.CharFilter(lookup_expr='icontains')
    year = django_filters.NumberFilter()
    year__gte = django_filters.NumberFilter(field_name='year', lookup_expr='gte')
    year__lte = django_filters.NumberFilter(field_name='year', lookup_expr='lte')

    class Meta:
        model = Car
        fields = [ 'model', 'year', 'price', 'status']
