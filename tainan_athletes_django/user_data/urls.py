from django.urls import path, include
from .views import LoginAPIView
# from .views import UserInfoAPIView

urlpatterns = [
	path("auth/login/", LoginAPIView.as_view(), name="login"),
	# path("user_info/", UserInfoAPIView.as_view(), name="user_info"), 
]
