# from django.contrib.auth.models import Group
# from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from .serializers import ProfileSerializer

from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
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
    is_expired, token = token_expire_handler(token)     # The implementation will be described further

    return Response({
        'user': user.username, 
        'expires_in': expires_in(token),
        'token': token.key
    }, status=HTTP_200_OK)


class UserGroupAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
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

