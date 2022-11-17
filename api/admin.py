from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Clinic)
admin.site.register(CareRoom)
admin.site.register(NurseryAppointment)
admin.site.register(PatientAppiontment)
admin.site.register(SurgicalAppointment)
admin.site.register(Bill)
admin.site.register(BloodBank)
admin.site.register(CentralCare)