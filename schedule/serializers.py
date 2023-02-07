from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Schedule
from . import models
from doctor.serializers import DoctorSerializer

class ScheduleSerializer(ModelSerializer):
    days  = serializers.MultipleChoiceField(choices=models.DAYS)
    class Meta:
        model = Schedule
        fields = '__all__'
        
class ShowScheduleSerializer(ModelSerializer):
    doctor = DoctorSerializer()
    class Meta:
        model = Schedule
        fields = '__all__'