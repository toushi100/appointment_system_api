from django.contrib import admin
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'middle_name', 'last_name', 'phone', 'date_of_birth', 'user')
admin.site.register(Doctor, DoctorAdmin)