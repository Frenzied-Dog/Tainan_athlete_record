# from django.contrib.auth.models import Group
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import (
    # HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
)

from .models import UserProfile
from .serializers import ProfileSerializer
from .authentication import expires_in, is_token_expired, token_expire_handler

@api_view(["POST"])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def signin(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username = username, password = password)
    
    if not user:
        return Response({'detail': 'Invalid Credentials or activate account'}, status=HTTP_404_NOT_FOUND)
        
    #TOKEN STUFF
    token, _ = Token.objects.get_or_create(user = user)

    # TODO Future: 提示有已登入的token
    # _, token = token_expire_handler(token)
    
    # always delete the old token
    token.delete()
    token = Token.objects.create(user = token.user)
    
    return Response({
        'user': user.username, 
        'name': user.profile.name,
        'group': user.profile.group.name,
        'expires_in': expires_in(token),
        'token': token.key,
    }, status=HTTP_200_OK)

@api_view(["POST"])
@permission_classes((AllowAny,))
def verify(request):
    key = request.data.get("token")
    token = Token.objects.get(key = key) if Token.objects.filter(key = key).exists() else None
    
    user = token.user if token else None
    if not user:
        return Response({'detail': 'Invalid Token'}, status=HTTP_401_UNAUTHORIZED)
    
    is_expired, token = token_expire_handler(token)
    if is_expired:
        return Response({'detail': 'The Token is expired'}, status=HTTP_401_UNAUTHORIZED)

    return Response({
        'user': user.username, 
        'is_valid': not is_expired,
        'expires_in': expires_in(token),
    }, status=HTTP_200_OK)

@api_view(["GET"])
def signout(request):
    user = request.user
    
    token, _ = Token.objects.get_or_create(user = user)
    
    token.delete()
    
    # 確保 舊token無法使用
    token = Token.objects.create(user = token.user)    
    
    return Response({
        'user': user.username, 
        'logout': True
    }, status=HTTP_200_OK)

@api_view(["GET"])
def getUserGroup(request):
    user = request.user
    
    return Response({
        "user": user.username,
        "name": user.profile.name,
        "group": user.profile.group.name,
    }, status=HTTP_200_OK)

@api_view(["GET"])
def getSelfProfile(request):
    user = request.user
    
    serializer = ProfileSerializer(user.profile)
    return Response(serializer.data)
    

class ProfileView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer

    # 只有管理員可以新增帳號
    def create(self, request, *args, **kwargs):
        usr = request.user
        
        if usr.is_staff:
            return super().create(request, *args, **kwargs)
        
        return Response({'error': 'You are not allowed to create profile.'}, status=HTTP_403_FORBIDDEN)


    def list(self, request, *args, **kwargs):
        usr = request.user
        
        if usr.is_staff:
            return super().list(request, *args, **kwargs)
        
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
            
            return Response({'error': 'You are not allowed to retrieve this profile.'}, status=HTTP_403_FORBIDDEN)
    
    
    def update(self, request, *args, **kwargs):
        usr = request.user
        
        if usr.is_staff:
            return super().update(request, *args, **kwargs)
        
        instance = self.get_object()
        if instance.user == usr or (usr.profile.group.name == 'Coach' and instance in usr.profile.linking.all()):
            return super().update(request, *args, **kwargs)
        
        return Response({'error': 'You are not allowed to update this profile.'}, status=HTTP_403_FORBIDDEN)
    
    
    def destroy(self, request, *args, **kwargs):
        usr = request.user
        
        if usr.is_staff:
            return super().destroy(request, *args, **kwargs)
        
        return Response({'error': 'You are not allowed to delete profile.'}, status=HTTP_403_FORBIDDEN)


from django.http import JsonResponse
import pandas as pd
import os

# 這是新的 API，專門用於提供數據給前端繪製圖表
def get_data(request):
    # CSV 檔案的路徑（請修改為實際的檔案路徑）
    file_path = os.path.join(os.path.dirname(__file__), 'BodyData.csv')

    # 讀取 CSV 資料
    data = pd.read_csv(file_path)

    # 將資料轉換為 JSON 格式回傳
    return JsonResponse(data.to_dict(orient='records'), safe=False)