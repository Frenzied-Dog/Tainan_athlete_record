from django.contrib import admin
from .models import Athlete, Coach, HurtRecord, RaceRecord, DailyTrainRecord

# Register your models here.
admin.site.register(Athlete)
admin.site.register(Coach)
admin.site.register(HurtRecord)
admin.site.register(RaceRecord)
admin.site.register(DailyTrainRecord)