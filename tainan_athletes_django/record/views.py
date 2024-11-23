from rest_framework import generics
from rest_framework import viewsets
from .models import RaceRecord, HurtRecord, BasicInfo, PhysicalTest
from .serializers import *




class RaceRecordView(viewsets.ModelViewSet):
    queryset = RaceRecord.objects.all()
    serializer_class = RaceRecordSerializer


class HurtRecordView(viewsets.ModelViewSet):
    queryset = HurtRecord.objects.all()
    serializer_class = HurtRecordSerializer
    
class BasicInfoView(viewsets.ModelViewSet):
    queryset = BasicInfo.objects.all()
    serializer_class = BasicInfoSerializer

class PhysicalTestView(viewsets.ModelViewSet):
    queryset = PhysicalTest.objects.all()
    serializer_class = PhysicalTestSerializer