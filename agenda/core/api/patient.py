from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.api.serializers import PatientSerializer
from core.models import Patient


class PatientViewSet(viewsets.ModelViewSet):
    "Serializers handler Patient"
    permission_classes = (IsAuthenticated,)
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    filterset_fields = "__all__"

    def create(self, request):
        return super().create(request)        

    def update(self, request, pk=None):
        return super().update(request, pk)        

    def delete(self, request):
        ...
        
    def get_queryset(self):
        ...

    def patient_filter(self, request):
        return Patient.objects.all()

    def get_queryset(self):
        queryset = self.patient_filter(self.request)
        return queryset        
        
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, 200)
