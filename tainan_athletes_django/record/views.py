from django.contrib.auth.models import User, Group
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
)

from .models import RaceRecord, HurtRecord, BasicInfo, PhysicalTest
from .serializers import *

class RecordViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        usr = request.user
        ath = User.objects.get(id=request.data.get('athlete'))
        
        if usr.is_staff:
            return super().create(request, *args, **kwargs)
        
        if ath.profile.group.name == 'Coach':
            return Response({'error': 'You cannot create record for coach.'}, status=status.HTTP_403_FORBIDDEN)
        
        if (usr.profile.group.name == 'Athlete' and ath != usr) or (usr.profile.group.name == 'Coach' and ath.profile not in usr.profile.linking.all()):
            return Response({'error': 'You are not allowed to create record for this athlete.'}, status=status.HTTP_403_FORBIDDEN)
        
        return super().create(request, *args, **kwargs)
    
    
    def list(self, request, *args, **kwargs):
        usr = request.user
        
        queryset = self.filter_queryset(self.get_queryset())
        if usr.is_staff:
            pass
        elif usr.profile.group.name == 'Coach':
            queryset = queryset.filter(athlete__in=usr.profile.linking.all())            
        else:
            queryset = queryset.filter(athlete=usr.profile)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, *args, **kwargs):
        usr = request.user
        if usr.is_staff:
            return super().retrieve(request, *args, **kwargs)
        
        #check if is retrieve own or linking profile
        instance = self.get_object()
        
        if instance.athlete == usr.profile or instance.athlete in usr.profile.linking.all():
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        
        return Response({'error': 'You are not allowed to retrieve this Record.'}, status=HTTP_403_FORBIDDEN)

    
    def update(self, request, *args, **kwargs):
        usr = request.user
        
        if usr.is_staff:
            return super().update(request, *args, **kwargs)
        
        instance = self.get_object()
        if instance.athlete == usr.profile or (usr.profile.group.name == 'Coach' and instance.athlete in usr.profile.linking.all()):
            # make athlete field unchangeable
            
            if request.data.get("athlete") not in (None, str(instance.athlete.user.id)):
                return Response({'error': 'You cannot change athlete field.'}, status=HTTP_400_BAD_REQUEST)
            
            return super().update(request, *args, **kwargs)
        
        return Response({'error': 'You are not allowed to update this record.'}, status=HTTP_403_FORBIDDEN)
    
    
    def destroy(self, request, *args, **kwargs):
        usr = request.user
        
        if usr.is_staff:
            return super().destroy(request, *args, **kwargs)

        #check if is retrieve own or linking profile
        instance = self.get_object()
        
        if instance.athlete == usr.profile or instance.athlete in usr.profile.linking.all():
            return super().destroy(request, *args, **kwargs)
        
        return Response({'error': 'You are not allowed to delete this record.'}, status=status.HTTP_403_FORBIDDEN)
        
        
class RaceRecordView(RecordViewSet):
    queryset = RaceRecord.objects.all()
    serializer_class = RaceRecordSerializer
    
class HurtRecordView(RecordViewSet):
    queryset = HurtRecord.objects.all()
    serializer_class = HurtRecordSerializer
    
class BasicInfoView(RecordViewSet):
    queryset = BasicInfo.objects.all()
    serializer_class = BasicInfoSerializer

class PhysicalTestView(RecordViewSet):
    queryset = PhysicalTest.objects.all()
    serializer_class = PhysicalTestSerializer