from django.db import models
from  patient.models import Patient

bed_choices = (('bed_1','Bed 1'),
               ('bed_2','Bed 2'),
               ('bed_3','Bed 3'),
               ('bed_4','Bed 4'),
               ('bed_5','Bed 5'),)

class IntensiveCareUnit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bed = models.CharField(max_length=100, choices=bed_choices)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    estimated_time = models.DateTimeField()
   
    def __str__(self):
        return f'{self.patient} {self.bed} {self.start_time} {self.end_time} {self.estimated_time}'