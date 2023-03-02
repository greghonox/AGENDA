from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import index, register_patient, remove_patient, \
query_patient, change_patient, register_doctor, query_doctor, change_doctor, remove_doctor, register_scheduler, query_scheduler, change_scheduler, remove_scheduler
from rest_framework import permissions, routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core.api.patient import PatientViewSet
from core.api.doctor import DoctorViewSet
from core.api.scheduler import ScheduleViewSet

route = routers.DefaultRouter()
route.register("patient", PatientViewSet, "patient")
route.register("doctor", DoctorViewSet, "doctor")
route.register("schedule", ScheduleViewSet, "schedule")


urlpatterns = [
    path('', index, name='home'),
    path('register_patient/', register_patient, name='register_patient'),
    path('query_patient/', query_patient, name='query_patient'),
    path('change_patient/<id>/', change_patient, name='change_patient'),
    path('remove_patient/<id>/', remove_patient, name='remove_patient'),
    
    path('register_doctor/', register_doctor, name='register_doctor'),
    path('query_doctor/', query_doctor, name='query_doctor'),
    path('change_doctor/<id>/', change_doctor, name='change_doctor'),
    path('remove_doctor/<id>/', remove_doctor, name='remove_doctor'),

    path('register_scheduler/', register_scheduler, name='register_scheduler'),
    path('query_scheduler/', query_scheduler, name='query_scheduler'),
    path('change_scheduler/<id>/', change_scheduler, name='change_scheduler'),
    path('remove_scheduler/<id>/', remove_scheduler, name='remove_scheduler'),
    path("api/", include(route.urls), name="api"),
    path("token/", TokenObtainPairView.as_view(), name="token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token/refresh"),
    
]