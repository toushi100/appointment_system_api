from django.db import models

# Create your models here.
care_room_type = [
    ('normal', 'Normal'),
    ('intensive', 'Intensive'),
]


class Doctor(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    patient_appiontment = models.CharField(max_length=100)
    examination_price = models.IntegerField()
    time_from = models.TimeField()
    time_to = models.TimeField()
    day = models.CharField(max_length=100)
    patient_appiontment = models.ManyToManyField(
        'PatientAppiontment', related_name='patient_appiontment', blank=True)
    clinc = models.ForeignKey('Clinic', on_delete=models.DO_NOTHING,
                              related_name='doctor_clinic', blank=True, null=True)
    care_room = models.ForeignKey('CareRoom', on_delete=models.DO_NOTHING)
    nursery_appiontment = models.ForeignKey('NurseryAppointment', on_delete=models.DO_NOTHING,
                                            related_name='nursery_appiontment', blank=True, null=True)
    def __str__(self):
        return self.name


class Clinic(models.Model):
    capacity = models.IntegerField()
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CareRoom(models.Model):
    patient_status = models.CharField(max_length=100)
    price = models.IntegerField()
    patient_name = models.CharField(max_length=100)
    available_room = models.CharField(max_length=100)
    national_id = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=care_room_type)

    def __str__(self):
        return self.name


class NurseryAppointment(models.Model):
    price = models.IntegerField()
    medical_note = models.CharField(max_length=1000)
    capacity = models.IntegerField()
    child_name = models.CharField(max_length=100)
    available_surgircal = models.CharField(max_length=100)
    busy_room = models.CharField(max_length=100)
    child_id = models.CharField(max_length=100)
    child_status = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    time_from = models.TimeField()
    time_to = models.TimeField()

    def __str__(self):
        return self.child_name


class PatientAppiontment(models.Model):
    patient_firstname = models.CharField(max_length=100)
    patient_middlename = models.CharField(max_length=100)
    patient_lastname = models.CharField(max_length=100)
    national_id = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    clinics = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    nursery_appointment = models.ForeignKey(
        NurseryAppointment, on_delete=models.DO_NOTHING, related_name='nursery_appointment', blank=True, null=True)
    blood_bank = models.ForeignKey(
        'BloodBank', on_delete=models.DO_NOTHING, related_name='blood_bank', blank=True, null=True)
    surgical_appointment = models.ForeignKey(
        'SurgicalAppointment', on_delete=models.DO_NOTHING, related_name='surgical_appointment', blank=True, null=True)
    

    def __str__(self):
        return self.patient_name


class BloodBank(models.Model):
    patient_name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    national_id = models.CharField(max_length=100)
    medical_history = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    anemia_rate = models.IntegerField()

    def __str__(self):
        return self.patient_name


class SurgicalAppointment(models.Model):
    patient_name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=100)
    medical_history = models.CharField(max_length=100)
    price = models.IntegerField()
    day = models.CharField(max_length=100)
    time_from = models.TimeField()
    time_to = models.TimeField()
    clinic = models.CharField(max_length=100)
    surgical_description = models.CharField(max_length=1000)
    doctor_name = models.CharField(max_length=100)
    available_room = models.CharField(max_length=100)
    patient_status = models.CharField(max_length=100)

    def __str__(self):
        return self.patient_name


class Bill(models.Model):
    patient_name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    total_price = models.IntegerField()
    nursery_price = models.IntegerField()
    surgical_price = models.IntegerField()
    doctor_price = models.IntegerField()
    central_care_price = models.IntegerField()
    care_room_price = models.IntegerField()
    patient_appiontment = models.ForeignKey(
        PatientAppiontment, on_delete=models.DO_NOTHING, related_name='appiontment', blank=True, null=True)

    def __str__(self):
        return self.patient_name


class CentralCare(models.Model):
    patient_name = models.CharField(max_length=100)
    service_name = models.CharField(max_length=100)
    price = models.IntegerField()
    patient_appiontment = models.ForeignKey(
        PatientAppiontment, on_delete=models.DO_NOTHING, related_name='central_care_appiontment', blank=True, null=True)

    def __str__(self):
        return self.patient_name
