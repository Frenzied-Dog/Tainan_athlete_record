# from django.contrib.auth.models import Group
# from rest_framework.permissions import IsAuthenticated

from rest_framework import generics
from .models import UserProfile
from .serializers import ProfileSerializer

from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class LoginAPIView(APIView):
    # def get(self, request):
    #     return Response({"message": "Login page"})
    
    def post(self, request, *args, **kwargs):
        # 從請求中獲取使用者名稱與密碼
        username = request.data.get("username")
        password = request.data.get("password")

        # 驗證用戶
        user = authenticate(username=username, password=password)
        
        if user:
            # 生成 JWT Tokens
            refresh = RefreshToken.for_user(user)
            # 獲取用戶所屬的 Group
            groups = [group.name for group in user.groups.all()]

            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "groups": groups,  # 返回用戶所屬群組
            })
        else:
            return Response({"error": "Invalid credentials"}, status=401)


class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer