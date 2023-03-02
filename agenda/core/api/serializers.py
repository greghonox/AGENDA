from rest_framework import serializers
from rest_framework.response import Response
from core.models import Doctor, Patient, Schedule
from datetime import datetime

class DoctorSerializer(serializers.ModelSerializer):
    """Class to Doctor"""

    class Meta:
        model = Doctor
        fields = "__all__"

    def __str__(self):
        return f"{self.full_name} {self.observation} ({self.crm})"


class PatientSerializer(serializers.ModelSerializer):
    """Class to PatientSerializer"""

    class Meta:
        model = Patient
        fields = "__all__"

    def __str__(self):
        return f"{self.full_name} {self.observation} ({self.id})"

class ScheduleSerializer(serializers.ModelSerializer):
    """Class to ScheduleSerializer"""

    dia = serializers.DateTimeField(source='date', format='%Y-%m-%d')
    hora = serializers.DateTimeField(source='date', format='%H:%M')
    data_agendamento = serializers.DateTimeField(source='date')
    doctor = DoctorSerializer()
    
    class Meta:
        model = Schedule
        fields = ('id', 'dia', 'hora', 'data_agendamento', 'doctor')
    
    def __str__(self):
        return f"{self.doctor} {self.patient} ({self.date})"