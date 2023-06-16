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

    def create(self, validated_data):
        get_blood_type = validated_data.get('blood_type')
        get_blood_row = BloodBank.objects.filter(blood_type=get_blood_type)
        if get_blood_row:
            get_blood_row = get_blood_row[0]
            get_blood_row.amount += validated_data.get('amount')
            get_blood_row.save()
            return get_blood_row
        else:
            BloodBank.objects.create(**validated_data)
            return validated_data


class BloodBankRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodbankRequest
        fields = '__all__'
    
    def create(self, validated_data):
        get_blood_type = validated_data.get('blood_type')
        get_blood_row = BloodBank.objects.filter(blood_type=get_blood_type)
        if get_blood_row:
            get_blood_row = get_blood_row[0]
            get_blood_row.amount -= validated_data.get('amount')
            get_blood_row.save()
            return get_blood_row
        else:
            return validated_data
