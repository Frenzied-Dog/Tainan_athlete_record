from django.contrib import admin
from .models import HurtRecord, RaceRecord, DailyTrainRecord

# Register your models here.
admin.site.register(HurtRecord)
admin.site.register(RaceRecord)
admin.site.register(DailyTrainRecord)