from django.db import models 
# Create your models here.
care_room_type = [
    ('normal', 'Normal'),
    ('intensive', 'Intensive'),
]
gender = [
    ('male', 'Male'),
    ('female', 'Female'),
]

class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    appointment_time_from = models.TimeField()
    appointment_time_to = models.TimeField()
    number_of_patients = models.IntegerField()
    phone = models.CharField(max_length=100)
    clinic = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    password = models.CharField(max_length=100)
    email = models.EmailField()
    experience = models.CharField(max_length=100)
    fees = models.IntegerField()
    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Clinic(models.Model):
    department = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    available_name = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='clinic_doctor')


class CareRoom(models.Model):
    numebr_of_days = models.IntegerField()
    patient_status = models.CharField(max_length=100)
    price = models.IntegerField()
    patient_name = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    available_room = models.CharField(max_length=100)
    care_room_type = models.CharField(max_length=100, choices=care_room_type)
    doctors = models.ForeignKey(to=Doctor, related_name='care_room_doctor', blank=True, on_delete=models.CASCADE)
    patients = models.ForeignKey(to='Patient', related_name='care_room_patient', blank=True, on_delete=models.CASCADE)



class Nursery(models.Model):
    phone = models.CharField(max_length=100)
    price = models.IntegerField()
    medical_note = models.CharField(max_length=1000)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    child_name = models.CharField(max_length=100)
    available_room = models.CharField(max_length=100)
    child_id = models.CharField(max_length=100)
    child_status = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    day_from = models.CharField(max_length=100)
    day_to = models.CharField(max_length=100)
    time_from = models.TimeField()
    time_to = models.TimeField()
    doctor = models.ManyToManyField(to=Doctor, related_name='nursery_doctor', blank=True)
    patient = models.ManyToManyField(to='Patient', related_name='nursery_patient', blank=True)

    def __str__(self):
        return self.child_name


class Patient(models.Model):
    patient_name = models.CharField(max_length=100)
    appointment = models.CharField(max_length=100)
    national_id = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=gender)
    doctors = models.ManyToManyField(to=Doctor, related_name='patient_doctor', through=CareRoom , blank=True)

    def __str__(self):
        return self.patient_name


class BloodBank(models.Model):
    patient_name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    national_id = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    anemia_name = models.IntegerField()
    order_id = models.IntegerField()
    doctors = models.ManyToManyField(to=Doctor, related_name='blood_bank_doctor', blank=True)


    def __str__(self):
        return self.patient_name


class SurgicalOperation(models.Model):
    available_room = models.CharField(max_length=100)
    patient_name = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    time = models.TimeField()
    clinic = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    surgical_description = models.CharField(max_length=1000)
    price = models.IntegerField()
    doctor_name = models.CharField(max_length=100)
    doctors  = models.ManyToManyField(to=Doctor, related_name='doctor', blank=True)


    def __str__(self):
        return self.patient_name


class Schedule(models.Model):
    doctor_name = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    time_from = models.TimeField()
    time_to = models.TimeField()
    date = models.DateField()
    patient_name = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='schedule_doctor')


class CentralCare(models.Model):
    patient_name = models.CharField(max_length=100)
    service_name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.patient_name
