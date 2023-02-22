from rest_framework import serializers
from .models import Incubator

class ShowIncubatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incubator
        fields = '__all__'
        depth = 1
        
class IncubatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incubator
        fields = '__all__'