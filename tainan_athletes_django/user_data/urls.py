from django.urls import path, include
from .views import LoginAPIView, get_data
# from .views import UserInfoAPIView

urlpatterns = [
	path("auth/login/", LoginAPIView.as_view(), name="login"),
	# path("user_info/", UserInfoAPIView.as_view(), name="user_info"), 
	path("api/data/", get_data, name="get_data"),  # 新增 API 路由
]
