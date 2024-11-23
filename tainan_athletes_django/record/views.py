from rest_framework import generics
from rest_framework import viewsets
from .models import DailyTrainRecord, RaceRecord, HurtRecord
from .serializers import DailyTrainRecordSerializer, RaceRecordSerializer, HurtRecordSerializer


class DailyTrainRecordView(viewsets.ModelViewSet):
    queryset = DailyTrainRecord.objects.all()
    serializer_class = DailyTrainRecordSerializer



class RaceRecordView(viewsets.ModelViewSet):
    queryset = RaceRecord.objects.all()
    serializer_class = RaceRecordSerializer


class HurtRecordView(viewsets.ModelViewSet):
    queryset = HurtRecord.objects.all()
    serializer_class = HurtRecordSerializer