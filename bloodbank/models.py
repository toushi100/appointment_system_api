from django.db import models
from patient.models import Patient
from django.db.models import Sum

BLOOD_TYPE_CHOICES = (('A+','A+'), 
                      ('A-','A-'),
                      ('B+','B+'), 
                      ('B-','B-'),
                      ('O+','O+'), 
                      ('O-','O-'),
                      ('AB+','AB+'), 
                      ('AB-','AB-'))

class BloodBankManager(models.Manager):
    def total_amount(self, blood_type):
        return self.get_queryset().filter(blood_type=blood_type).aggregate(Sum('amount'))
class BloodBank(models.Model):
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    amount = models.IntegerField()
    objects = BloodBankManager()
    
class BloodbankRequest(models.Model):
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    