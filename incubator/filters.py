import django_filters
from .models import Incubator

class IncubatorFilter(django_filters.FilterSet):
    patient = django_filters.NumberFilter(field_name='patient', lookup_expr='exact')
    incubator = django_filters.CharFilter(field_name='incubator', lookup_expr='exact')
    start_date__gte = django_filters.DateFilter(field_name='start_date', lookup_expr='gte')
    
    class Meta:
        model = Incubator
        fields ='__all__'