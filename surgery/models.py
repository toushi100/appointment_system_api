from django.db import models
from doctor.models import Doctor
from patient.models import Patient
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
ROOM_CHOICES = (
    ('OR_1', 'Operation Room 1'),
    ('OR_2', 'Operation Room 2'),
    ('OR_3', 'Operation Room 3'),
)


def validate_start_time_end_time(value):
    if value < timezone.now():
        raise ValidationError(
            _('%(value)s is not a valid start time'),
            params={'value': value},
        )


class Surgery(models.Model):
    doctors = models.ManyToManyField(Doctor)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    room = models.CharField(max_length=100, choices=ROOM_CHOICES)
    start_time = models.DateTimeField(
        validators=[validate_start_time_end_time])
    end_time = models.DateTimeField(validators=[validate_start_time_end_time])
    surgery_type = models.ForeignKey('SurgeryType', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Surgery'
        verbose_name_plural = 'Surgeries'

    def clean(self):
        if self.start_time > self.end_time:
            raise ValidationError("Start time must be before end time.")

        if Surgery.objects.filter(start_time__lte=self.start_time, end_time__gte=self.start_time, room=self.room).exists():
            raise ValidationError("Surgery overlaps with another surgery.")

        if Surgery.objects.filter(start_time__lte=self.end_time, end_time__gte=self.end_time, room=self.room).exists():
            raise ValidationError("Surgery overlaps with another surgery.")


class SurgeryType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Surgery Type'
        verbose_name_plural = 'Surgery Types'
