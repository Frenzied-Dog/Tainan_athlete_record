from rest_framework import generics
from .models import DailyTrainRecord, RaceRecord, HurtRecord
from .serializers import DailyTrainRecordSerializer, RaceRecordSerializer, HurtRecordSerializer


class DailyTrainRecordListCreateView(generics.ListCreateAPIView):
    queryset = DailyTrainRecord.objects.all()
    serializer_class = DailyTrainRecordSerializer


class DailyTrainRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyTrainRecord.objects.all()
    serializer_class = DailyTrainRecordSerializer


class RaceRecordListCreateView(generics.ListCreateAPIView):
    queryset = RaceRecord.objects.all()
    serializer_class = RaceRecordSerializer


class RaceRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RaceRecord.objects.all()
    serializer_class = RaceRecordSerializer


class HurtRecordListCreateView(generics.ListCreateAPIView):
    queryset = HurtRecord.objects.all()
    serializer_class = HurtRecordSerializer


class HurtRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HurtRecord.objects.all()
    serializer_class = HurtRecordSerializer
