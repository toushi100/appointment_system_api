from django.db import models
from user.models import User


class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    speciality = models.ForeignKey('Speciality', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Speciality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Speciality'
        verbose_name_plural = 'Specialities'