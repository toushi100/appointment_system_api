from django.db import models
from user.models import User

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50, unique=True, null=True)
    date_of_birth = models.DateField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')