from rest_framework import serializers
from .models import Surgery

class ShowSurgerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Surgery
        fields = '__all__'
        depth = 1

class SurgerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Surgery
        fields = '__all__'