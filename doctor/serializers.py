from  rest_framework import serializers
from . models import Doctor, Speciality


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        
class ShowDoctorSerializer(DoctorSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        depth = 1
        
class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = '__all__'