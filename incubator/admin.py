from django.contrib import admin
from .models import Incubator

class IncubatorAdmin(admin.ModelAdmin):
    list_display = ('patient', 'start_date', 'end_date', 'incubator')
    list_filter = ('incubator', 'start_date', 'end_date')
    search_fields = ('patient__first_name', 'patient__last_name', 'patient__id')
    
admin.site.register(Incubator, IncubatorAdmin)