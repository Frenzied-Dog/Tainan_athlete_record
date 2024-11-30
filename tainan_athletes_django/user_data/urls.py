from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileView, getUserGroup, getSelfProfile, signin, signout, verify, get_data, get_csrf

router = DefaultRouter(trailing_slash=False)
router.register(r'profile', ProfileView, basename='profile')

urlpatterns = [
    path("info/", getUserGroup, name="get-users-group"),
    path("self/", getSelfProfile, name="get-self-profile"),
    path("auth/csrf/", get_csrf, name="csrf"),
	path("auth/login/", signin, name="signin"),
    path("auth/logout/", signout, name="signout"),
	path("auth/verify/", verify, name="verify-token"),
    path('', include(router.urls), name='profile-list'),
    
	path("api/data/", get_data, name="get_data"),  # 新增 API 路由
]