import django_filters
from .models import BloodBank

class BloodBankFilter(django_filters.FilterSet):
    blood_type = django_filters.CharFilter(field_name="blood_type" ,lookup_expr='exact')
    class Meta:
        model = BloodBank
        fields = ['blood_type']