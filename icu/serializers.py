from rest_framework import serializers
from .models import IntensiveCareUnit

class IntensiveCareUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntensiveCareUnit
        fields = '__all__'
        
class showIntensiveCareUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntensiveCareUnit
        fields = '__all__'
        depth = 1