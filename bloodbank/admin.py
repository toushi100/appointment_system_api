from django.contrib import admin
from .models import BloodBank

class BloodBankAdmin(admin.ModelAdmin):
    list_display = ('id', 'blood_type', 'amount')

admin.site.register(BloodBank, BloodBankAdmin)