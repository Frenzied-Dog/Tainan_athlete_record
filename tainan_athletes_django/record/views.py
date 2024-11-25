from django.contrib.auth.models import User, Group
from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import RaceRecord, HurtRecord, BasicInfo, PhysicalTest
from .serializers import *


class RaceRecordView(viewsets.ModelViewSet):
    queryset = RaceRecord.objects.all()
    serializer_class = RaceRecordSerializer

    def create(self, request, *args, **kwargs):
        
        ath = User.objects.get(id=request.data.get('athlete'))
        if ath not in ([request.user] + [i for i in request.user.profile.linking.all()]):
            return Response({'error': 'You are not allowed to create record for other athletes.'}, status=status.HTTP_403_FORBIDDEN)
        
        return super().create(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        
        if self.get_object().athlete.id not in ([request.user.id] + [i.id for i in request.user.profile.linking.all()]):
            return Response({'error': 'You are not allowed to delete record for other athletes.'}, status=status.HTTP_403_FORBIDDEN)
        
        return super().destroy(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if request.user.is_stuff:
            pass
        elif request.user.profile.group.name == 'Coach':
            queryset = queryset.filter(athlete__in=request.user.profile.linking.all())            
        else:
            queryset = queryset.filter(athlete=request.user)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class HurtRecordView(viewsets.ModelViewSet):
    queryset = HurtRecord.objects.all()
    serializer_class = HurtRecordSerializer
    
class BasicInfoView(viewsets.ModelViewSet):
    queryset = BasicInfo.objects.all()
    serializer_class = BasicInfoSerializer

class PhysicalTestView(viewsets.ModelViewSet):
    queryset = PhysicalTest.objects.all()
    serializer_class = PhysicalTestSerializer