from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

class LoginAPIView(APIView):
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


# class UserInfoAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         user = request.user
#         groups = [group.name for group in user.groups.all()]  # 獲取用戶所屬群組

#         return Response({
#             "username": user.username,
#             # "email": user.email,
#             "groups": groups,
#         })

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
