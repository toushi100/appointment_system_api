from rest_framework import serializers
from . models import User 
from patient.serializers import PatientSerializer
from doctor.serializers import DoctorSerializer

class UserSerializer(serializers.ModelSerializer):

    patient = serializers.SerializerMethodField()
    doctor = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'
        
        extra_kwargs = {'password': {'write_only': True}}

    def get_patient(self, obj):
        try:
            patient = obj.patient
            serializer = PatientSerializer(patient)
            return serializer.data
        except:
            return None
    
    def get_doctor(self, obj):
        try:
            patient = obj.doctor
            serializer = DoctorSerializer(patient)
            return serializer.data 
        except:
            return None
 
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance