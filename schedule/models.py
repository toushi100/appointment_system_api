from django.db import models
from multiselectfield import MultiSelectField
from doctor.models import Doctor
# Create your models here.
DAYS = (
    ("sat", "Saturday"),
    ("sun", "Sunday"),
    ("mon", "Monday"),
    ("tue", "Tuesday"),
    ("wed", "Wednesday"),
    ("thu", "Thursday"),
    ("fri", "Friday")
)

class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    days = MultiSelectField(choices=DAYS,max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    def __str__(self):
        return self.doctor.first_name
    
class Appointment(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    # patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    def __str__(self):
        # title  = f'{self.patient.id} {self.patient.name} {self.schedule.doctor.name} {self.start_time.strftime("%d/%m/%Y %H:%M")} '
        
        return self.schedule.doctor.first_name