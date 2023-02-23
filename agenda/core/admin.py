from django.contrib import admin
from .models import Patient, Doctor, Schedule
from core.forms import ScheduleForm

class DoctorAdmin(admin.ModelAdmin):
    list_filter = ['full_name', 'observation', 'special',]
    list_display = list_filter

class PatientAdmin(admin.ModelAdmin):
    list_filter = ['full_name', 'observation']
    list_display = list_filter

class ScheduleAdmin(admin.ModelAdmin):
    list_filter = ['doctor', 'patient', 'date']
    list_display = list_filter
    form = ScheduleForm

admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Schedule, ScheduleAdmin)