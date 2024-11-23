from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileView, UserGroupAPIView, signin, signout

router = DefaultRouter(trailing_slash=False)
router.register(r'profile', ProfileView, basename='profile')

urlpatterns = [
    path("info/", UserGroupAPIView.as_view(), name="get-users-group"),
	path("auth/login/", signin, name="signin"),
    path("auth/logout/", signout, name="signout"),
    path('/', include(router.urls), name='profile-list')
]