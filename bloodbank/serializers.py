from rest_framework import serializers
from .models import BloodBank, BloodbankRequest

class ShowBloodBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodBank
        fields = '__all__'
        depth = 1

class BloodBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodBank
        fields = '__all__'
        
class BloodBankRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodbankRequest
        fields = '__all__'