from django.db import models
from user.models import User
# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    user = models.OneToOneField(User,  on_delete=models.CASCADE) 
    def __str__(self):
        return self.first_name + ' ' + self.last_name
