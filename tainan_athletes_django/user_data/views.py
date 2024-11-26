# from django.contrib.auth.models import Group
# from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from .serializers import ProfileSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
)
from rest_framework.response import Response

from .serializers import ProfileSerializer
from .authentication import token_expire_handler, expires_in

@api_view(["POST"])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def signin(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(
            username = username,
            password = password 
        )
    
    if not user:
        return Response({'detail': 'Invalid Credentials or activate account'}, status=HTTP_404_NOT_FOUND)
        
    #TOKEN STUFF
    token, _ = Token.objects.get_or_create(user = user)

    #token_expire_handler will check, if the token is expired it will generate new one
    # TODO Future: 提示有已登入的token
    # _, token = token_expire_handler(token)
    
    # always delete the old token
    token.delete()
    token = Token.objects.create(user = token.user)
    
    return Response({
        'user': user.username, 
        'expires_in': expires_in(token),
        'token': token.key
    }, status=HTTP_200_OK)


@api_view(["GET"])
def signout(request):
    user = request.user
    
    token, _ = Token.objects.get_or_create(user = user)
    
    token.delete()
    token = Token.objects.create(user = token.user)    
    
    return Response({
        'user': user.username, 
        'logout': True
    }, status=HTTP_200_OK)


@api_view(["GET"])
def getUserGroup(self, request, *args, **kwargs):
    user = request.user
    groups = [group.name for group in user.groups.all()]  # 獲取用戶所屬群組

    return Response({
        "username": user.username,
        "email": user.email,
        "groups": groups,
    })


class ProfileView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer

    def create(self, request, *args, **kwargs):        
        usr = request.user
        
        if usr.is_staff:
            return super().create(request, *args, **kwargs)
        else:
            return Response({'error': 'You are not allowed to create profile.'}, status=HTTP_403_FORBIDDEN)


    def list(self, request, *args, **kwargs):
        usr = request.user
        
        if usr.is_staff:
            return super().list(request, *args, **kwargs)
        else:
            queryset = self.filter_queryset(self.get_queryset())
            queryset = queryset.filter(user__in=usr.profile.linking.all())
            
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
    
    
    def retrieve(self, request, *args, **kwargs):
        usr = request.user
        
        if usr.is_staff:
            return super().retrieve(request, *args, **kwargs)
        else:
            #check if is retrieve own or linking profile
            instance = self.get_object()
            
            if instance in usr.profile.linking.all() or instance.user == usr:
                serializer = self.get_serializer(instance)
                return Response(serializer.data)
            else:
                return Response({'error': 'You are not allowed to retrieve this profile.'}, status=HTTP_403_FORBIDDEN)
    
    
    def update(self, request, *args, **kwargs):
        usr = request.user
        
        if usr.is_staff:
            return super().update(request, *args, **kwargs)
        else:
            instance = self.get_object()
            
            if instance.user == usr or (usr.profile.group.name == 'Coach' and instance in usr.profile.linking.all()):
                return super().update(request, *args, **kwargs)
            else:
                return Response({'error': 'You are not allowed to update this profile.'}, status=HTTP_403_FORBIDDEN)
    
    
    def destroy(self, request, *args, **kwargs):
        usr = request.user
        
        if usr.is_staff:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response({'error': 'You are not allowed to delete profile.'}, status=HTTP_403_FORBIDDEN)