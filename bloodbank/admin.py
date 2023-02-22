from django.contrib import admin
from .models import BloodBank

class BloodBankAdmin(admin.ModelAdmin):
    list_display = ('id','patient', 'blood_type', 'donated_amount', 'date')

admin.site.register(BloodBank, BloodBankAdmin)