from django.contrib import admin
from .models import Schedule, Appointment


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'doctor', 'days', 'start_time', 'end_time')


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'schedule', 'patient', 'start_time', 'end_time')


admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Appointment, AppointmentAdmin)
