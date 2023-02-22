from django.db import models
from patient.models import Patient
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta, date


INCUBATOR_CHOICES = (('nicu_1', 'Incubator 1'),
                     ('nicu_2', 'Incubator 2'),
                     ('nicu_3', 'Incubator 3'),
                     ('nicu_4', 'Incubator 4'),
                     ('nicu_5', 'Incubator 5'))


class Incubator(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    incubator = models.CharField(max_length=100, choices=INCUBATOR_CHOICES)

    def clean(self):
        if self.start_date and self.end_date and self.start_date > self.end_date:
            raise ValidationError('Start date must be before end date.')

        if date.today() - self.patient.date_of_birth >= timedelta(days=365):
            raise ValidationError('Patient is not eligible for NICU')

        qs = Incubator.objects.filter(
            start_date__lte=self.start_date, end_date__isnull=True, incubator=self.incubator)
        if self.pk:
            qs = qs.exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError("This incubator is not available for this time.")
