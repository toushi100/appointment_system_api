from django.contrib import admin
from .models import Surgery, SurgeryType


class SurgeryAdmin(admin.ModelAdmin):
    list_display = ('room', 'start_time', 'end_time',  'patient')
    list_filter = ('room', 'start_time', 'end_time')
    search_fields = ('room', 'start_time', 'end_time')
    ordering = ('room', 'start_time', 'end_time')


class SurgeryTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


admin.site.register(Surgery, SurgeryAdmin)
admin.site.register(SurgeryType, SurgeryTypeAdmin)
