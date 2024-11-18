from django.urls import path
from .views import (
    DailyTrainRecordListCreateView,
    DailyTrainRecordDetailView,
    RaceRecordListCreateView,
    RaceRecordDetailView,
    HurtRecordListCreateView,
    HurtRecordDetailView,
)

urlpatterns = [
    path('daily-train-records/', DailyTrainRecordListCreateView.as_view(), name='daily-train-record-list-create'),
    path('daily-train-records/<int:pk>/', DailyTrainRecordDetailView.as_view(), name='daily-train-record-detail'),
    path('race-records/', RaceRecordListCreateView.as_view(), name='race-record-list-create'),
    path('race-records/<int:pk>/', RaceRecordDetailView.as_view(), name='race-record-detail'),
    path('hurt-records/', HurtRecordListCreateView.as_view(), name='hurt-record-list-create'),
    path('hurt-records/<int:pk>/', HurtRecordDetailView.as_view(), name='hurt-record-detail'),
]
