from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.api.serializers import ScheduleSerializer
from core.models import Schedule
from datetime import datetime
from rest_framework import serializers

class ScheduleViewSet(viewsets.ModelViewSet):
    "Serializers handler Schedule"
    permission_classes = (IsAuthenticated,)
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()
    filterset_fields = "__all__"

    def create(self, request):
        self.validation(request)
        return super().create(request)        
    
    def update(self, request, pk=None):
        self.validation(request)
        return super().update(request, pk)        

    def delete(self, request):
        ...
        
    def get_queryset(self):
        ...

    def schedule_filter(self, request):
        return Schedule.objects.all()

    def get_queryset(self):
        queryset = self.schedule_filter(self.request)
        return queryset        
        
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, 200)

    def validation(self, request):
        date = request.data['date']
        doctor = request.data['doctor']
        patient = request.data['patient']
        date = datetime.fromisoformat(date)
        
        if datetime.utcnow() > date:
            raise serializers.ValidationError('Não pode fazer agendamento antes da data corrente!')
        if len(self.get_schedule_hour(doctor, patient, date)) > 0:
            raise serializers.ValidationError(f'O agendamento para {patient} com o doutor: {doctor} já existe na data: {date}')      
        
    def get_schedule_hour(self, doctor, patient, date):
        data_start = datetime(date.year, date.month, date.day, date.hour, 0)
        data_end = datetime(date.year, date.month, date.day, date.hour, 59)
        return Schedule.objects.filter(date__range=(data_start, data_end), doctor=doctor, patient=patient)        