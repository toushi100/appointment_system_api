from django.db import models
from doctor.models import Doctor
from patient.models import Patient
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import timedelta
ROOM_CHOICES = (
    ('OR_1', 'Operation Room 1'),
    ('OR_2', 'Operation Room 2'),
    ('OR_3', 'Operation Room 3'),
)

surgery_type_choices = (
    ('1', 'Heart Surgery'),
    ('2', 'Brain Surgery'),
    ('3', 'Cancer Surgery'),
    ('4', 'Lung Surgery'),
    ('5', 'Other'),
)

    
class Surgery(models.Model):
    doctors = models.ManyToManyField(Doctor)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    room = models.CharField(max_length=100, choices=ROOM_CHOICES)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    estimated_time = models.DurationField(default=timedelta(minutes=30))
    surgery_type = models.CharField(max_length=100, choices=surgery_type_choices, default='5')
    notes = models.TextField(blank=True, null=True)
    

    class Meta:
        verbose_name = 'Surgery'
        verbose_name_plural = 'Surgeries'

    def clean(self):
        
        if self.end_time and self.start_time > self.end_time:
            raise ValidationError("Start time must be before end time.")

        if self.pk is None and Surgery.objects.filter(end_time=None, room=self.room).exists():
            raise ValidationError("Surgery overlaps with another surgery.")


