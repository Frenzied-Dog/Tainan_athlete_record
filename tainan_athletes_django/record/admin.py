from django.contrib import admin
from .models import HurtRecord, RaceRecord, BasicInfo, PhysicalTest

# Register your models here.
admin.site.register(HurtRecord)
admin.site.register(RaceRecord)
admin.site.register(BasicInfo)
admin.site.register(PhysicalTest)