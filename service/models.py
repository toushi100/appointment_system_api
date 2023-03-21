from django.db import models
from patient.models import Patient

SERVICE_CHOICES = (('injection', 'Injection'),
                   ('solution', 'Solution'),
                   ('wound_dressing', 'Wound Dressing'),)
# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    patient = models.ForeignKey('patient.Patient', on_delete=models.CASCADE)
    time = models.DateTimeField()
