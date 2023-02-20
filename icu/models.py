from django.db import models
from patient.models import Patient
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


bed_choices = (('bed_1', 'Bed 1'),
               ('bed_2', 'Bed 2'),
               ('bed_3', 'Bed 3'),
               ('bed_4', 'Bed 4'),
               ('bed_5', 'Bed 5'),)


class IntensiveCareUnit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bed = models.CharField(max_length=100, choices=bed_choices)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(default=None, blank=True, null=True)
    estimated_time = models.DurationField(
        default=timedelta(hours=8), blank=True, null=True)

    def __str__(self):
        return f'{self.patient} {self.bed} {self.start_time} {self.end_time} {self.estimated_time}'

    def clean(self):
        qs = IntensiveCareUnit.objects.filter(
            start_time__lte=self.start_time, end_time__isnull=True, bed=self.bed)
        if self.pk:
            qs = qs.exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError("No available ICU bed for this time.")
        if self.end_time is not None:
            if self.end_time < self.start_time:
                raise ValidationError(
                    "End time must be greater than start time.")
        if not self.pk:
            if self.start_time < timezone.now() - timedelta(minutes=1):
                raise ValidationError(
                    "Start time must be greater than current time.")
