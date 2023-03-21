import django_filters
from .models import Doctor

class DoctorFilter(django_filters.FilterSet):
    speciality = django_filters.CharFilter(field_name="speciality",lookup_expr='exact')
    
    class Meta:
        model = Doctor
        fields = ['speciality']