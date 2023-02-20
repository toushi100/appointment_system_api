import django_filters
from .models import IntensiveCareUnit

class IntensiveCareUnitFilter(django_filters.FilterSet):
    patient = django_filters.NumberFilter(field_name='patient', lookup_expr='exact')
    bed = django_filters.CharFilter(field_name='bed', lookup_expr='exact')
    estimated_time__gte = django_filters.DurationFilter(field_name='estimated_time', lookup_expr='gte')
    estimated_time__lte = django_filters.DurationFilter(field_name='estimated_time', lookup_expr='lte')
    
    class Meta:
        model = IntensiveCareUnit
        fields ='__all__'