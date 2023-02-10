from .models import Schedule
from datetime import timedelta
from datetime import datetime as dt
from .signals import CreateAppointement

def add_weekly_schedule():
    weekday = dt.today().strftime("%a").lower()
    schedule_for_next_week = Schedule.objects.filter(days__contains = weekday)
    for schedule in schedule_for_next_week:
        appointement = CreateAppointement(schedule.start_time, schedule.end_time, [weekday] ,schedule.id)
        appointement.run()
 