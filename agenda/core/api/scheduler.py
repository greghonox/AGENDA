from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.api.serializers import ScheduleSerializer
from core.models import Schedule, Doctor, Patient
from datetime import datetime, timezone
from rest_framework import serializers
from django.db.models import Q


class ScheduleViewSet(viewsets.ModelViewSet):
    "Serializers handler Schedule"
    permission_classes = (IsAuthenticated,)
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()
    filterset_fields = "__all__"

    def create(self, request):
        self.validation(request)
        data = request.data
        doctor = Doctor.objects.get(pk=data['doctor'])
        patient = Patient.objects.get(pk=data['patient'])
        schedule = Schedule(doctor=doctor, patient=patient, date=data['date'])
        schedule.save()
        return Response(status=202)
    
    def update(self, request, pk=None):
        data = request.data
        doctor = Doctor.objects.get(pk=data['doctor'])
        patient = Patient.objects.get(pk=data['patient'])
        schedule = Schedule.objects.filter(pk=pk)
        schedule.update(doctor=doctor, patient=patient, date=data['date'])
        return Response(status=203)

    def delete(self, request):
        ...

    def schedule_filter(self):
        now = datetime.now()
        parameters = self._build_query_parameters()
        if parameters:
            return Schedule.objects.filter(parameters).order_by('date')
        return  Schedule.objects.filter(date__gt=now).order_by('date')

    def _build_query_parameters(self):
        data_inicio = self.request.GET.get('data_inicio', [])
        data_final = self.request.GET.get('data_final', [])
        medico = self.request.query_params.getlist('medico')
        crm = self.request.query_params.getlist('crm')
        fields = [data_inicio, data_final, medico, crm]
        if any([len(query) > 0 for query in fields]):
            filters = Q()
            if data_inicio:
                filters &= Q(date__date__gte=data_inicio)

            if data_final:
                filters &= Q(date__date__lte=data_final)

            if medico:
                filters &= Q(doctor__in=medico)

            if crm:
                filters &= Q(doctor__crm__in=crm)
            return filters
        else:
            return {}
        
    def list(self, request):
        queryset = self.schedule_filter()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, 200)

    def validation(self, request):
        date = request.data['date']
        doctor = request.data['doctor']
        patient = request.data['patient']
        date = datetime.fromisoformat(date)
        
        if datetime.utcnow().replace(tzinfo=timezone.utc) > date:
            raise serializers.ValidationError('Não pode fazer agendamento antes da data corrente!')
        if len(self.get_schedule_hour(doctor, patient, date)) > 0:
            raise serializers.ValidationError(f'O agendamento para {patient} com o doutor: {doctor} já existe na data: {date}')      
        
    def get_schedule_hour(self, doctor, patient, date):
        data_start = datetime(date.year, date.month, date.day, date.hour, 0).replace(tzinfo=timezone.utc)
        data_end = datetime(date.year, date.month, date.day, date.hour, 59).replace(tzinfo=timezone.utc)
        return Schedule.objects.filter(date__range=(data_start, data_end), doctor=doctor, patient=patient)        