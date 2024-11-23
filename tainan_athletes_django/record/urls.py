from rest_framework.routers import DefaultRouter

from django.urls import path, include
from .views import (
    DailyTrainRecordView,
    RaceRecordView,
    HurtRecordView,
)

router = DefaultRouter()
router.register(r'DailyTrain', DailyTrainRecordView, basename='daily-train-record')
router.register(r'Race', RaceRecordView, basename='race-record')
router.register(r'Hurt', HurtRecordView, basename='hurt-record')

urlpatterns = [
    path('', include(router.urls), name='record-list'),
]
