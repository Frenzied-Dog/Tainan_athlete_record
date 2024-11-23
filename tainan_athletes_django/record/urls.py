from rest_framework.routers import DefaultRouter

from django.urls import path, include
from .views import (
    RaceRecordView,
    HurtRecordView,
    BasicInfoView,
    PhysicalTestView,
)

router = DefaultRouter(trailing_slash=False)

router.register(r'Race', RaceRecordView, basename='race-record')
router.register(r'Hurt', HurtRecordView, basename='hurt-record')
router.register(r'BasicInfo', BasicInfoView, basename='basic-info-record')
router.register(r'PhysicalTest', PhysicalTestView, basename='physical-record')

urlpatterns = [
    path('/', include(router.urls), name='record-list'),
]
