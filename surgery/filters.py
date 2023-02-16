import django_filters
from .models import Surgery

class SurgeryFilter(django_filters.FilterSet):
    doctor = django_filters.NumberFilter(field_name='doctor', lookup_expr='exact')
    surgery_type = django_filters.NumberFilter(field_name='surgery_type', lookup_expr='exact')
    
    class Meta:
        model = Surgery
        fields = ['surgery_type', 'doctor']