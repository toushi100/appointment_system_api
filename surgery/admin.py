from django.contrib import admin
from .models import Surgery

class SurgeryAdmin(admin.ModelAdmin):
    list_display = ('room', 'start_time', 'end_time',  'patient')
    list_filter = ('room', 'start_time', 'end_time')
    search_fields = ('room', 'start_time', 'end_time')
    ordering = ('room', 'start_time', 'end_time') 
    
admin.site.register(Surgery, SurgeryAdmin) 