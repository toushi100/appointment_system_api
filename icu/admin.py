from django.contrib import admin
from .models import IntensiveCareUnit

class IntensiveCareUnitAdmin(admin.ModelAdmin):
    list_display = ('patient', 'bed', 'start_time', 'end_time', 'estimated_time')
    
admin.site.register(IntensiveCareUnit, IntensiveCareUnitAdmin)
