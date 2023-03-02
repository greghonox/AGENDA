from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions, routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core.api.patient import PatientViewSet
from core.api.doctor import DoctorViewSet
from core.api.scheduler import ScheduleViewSet

route = routers.DefaultRouter()
route.register("patient", PatientViewSet, "patient")
route.register("doctor", DoctorViewSet, "doctor")
route.register("consultas", ScheduleViewSet, "schedule")


urlpatterns = [
    path("api/", include(route.urls), name="api"),
    path("token/", TokenObtainPairView.as_view(), name="token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token/refresh"),
    
]