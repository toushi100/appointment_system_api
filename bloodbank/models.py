from django.db import models
from patient.models import Patient

BLOOD_TYPE_CHOICES = (('A+','A+'), 
                      ('A-','A-'),
                      ('B+','B+'), 
                      ('B-','B-'),
                      ('O+','O+'), 
                      ('O-','O-'),
                      ('AB+','AB+'), 
                      ('AB-','AB-'))
class BloodBank(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    donated_amount = models.IntegerField()
    date = models.DateField()
    