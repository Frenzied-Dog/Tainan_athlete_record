from django.urls import path, include
from .views import LoginAPIView
from .views import ProfileListCreateView, ProfileDetailView

urlpatterns = [
	path("auth/login/", LoginAPIView.as_view(), name="login"),
    path('profile/', ProfileListCreateView.as_view(), name='profile-list-create'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
]