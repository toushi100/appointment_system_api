from django.contrib import admin
from .models import Doctor, Speciality

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'middle_name', 'last_name', 'phone', 'date_of_birth', 'user', 'speciality')
    
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Speciality, SpecialityAdmin)