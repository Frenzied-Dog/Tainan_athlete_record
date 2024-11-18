from django.urls import path, include
from .views import LoginAPIView
from .views import AthleteListCreateView, AthleteDetailView, CoachListCreateView, CoachDetailView

urlpatterns = [
	path("auth/login/", LoginAPIView.as_view(), name="login"),
    path('athletes/', AthleteListCreateView.as_view(), name='athlete-list-create'),
    path('athletes/<int:pk>/', AthleteDetailView.as_view(), name='athlete-detail'),
    path('coaches/', CoachListCreateView.as_view(), name='coach-list-create'),
    path('coaches/<int:pk>/', CoachDetailView.as_view(), name='coach-detail'),
]