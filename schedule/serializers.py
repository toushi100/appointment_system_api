from rest_framework  import serializers
from rest_framework import serializers
from .models import Schedule, Appointment
from . import models
from doctor.serializers import DoctorSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    days  = serializers.MultipleChoiceField(choices=models.DAYS)
    class Meta:
        model = Schedule
        fields = '__all__'
        
class ShowScheduleSerializer(serializers.ModelSerializer):

    days = serializers.MultipleChoiceField(choices=models.DAYS)
    doctor = DoctorSerializer()
    appointments = serializers.SerializerMethodField()
    class Meta:
        model = Schedule
        fields = '__all__'
    
    def get_appointments(self, obj):
        appointments = obj.appointment_set.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return serializer.data