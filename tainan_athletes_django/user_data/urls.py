from django.urls import path, include
from .views import ProfileView, UserGroupAPIView, signin, signout
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profile', ProfileView, basename='profile')

urlpatterns = [
    path("info/", UserGroupAPIView.as_view(), name="get-users-group"),
	path("auth/login/", signin, name="signin"),
    path("auth/logout/", signout, name="signout"),
    path('', include(router.urls), name='profile-list')
]