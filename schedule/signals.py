from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Schedule, Appointment
from datetime import timedelta
import datetime as dt
import pytz

@receiver(post_save, sender=Schedule)
def create_profile(sender, instance, created, **kwargs):
    if created:
        appointement = CreateAppointement(instance.start_time, instance.end_time, instance.days,instance.id)
        appointement.run()
        

class CreateAppointement:
    def __init__(self, start_time, end_time, days,schedule_id):
        self.start_time = start_time
        self.end_time =   end_time
        self.days = days
        self.schedule_id = schedule_id

    def run(self):
        dates = self.get_working_dates(self.days)
        for date in dates:
            start_datetime = dt.datetime.combine(date, self.start_time, tzinfo=pytz.UTC)
            end_datetime = dt.datetime.combine(date, self.end_time, tzinfo=pytz.UTC)
            slots = self.create_available_slots(start_datetime, end_datetime)
            for start_time,end_time in slots:
                Appointment.objects.create(schedule_id=self.schedule_id,start_time=start_time, end_time=end_time)
        
    def create_available_slots(self, start_time, end_time):
        slots = []
        while start_time < end_time:
            end_time_mod = start_time + timedelta(minutes=30)
            slots.append([start_time, end_time_mod])
            start_time = end_time_mod
        return slots
    
    def get_working_dates(self, days):
        dates = []
        today = dt.date.today()
        a_week_from_today = today + timedelta(days=7)
        while today <= a_week_from_today:
            if today.strftime("%a").lower() in days:
                dates.append(today)
            today += timedelta(days=1)
        return dates