from django import forms
import datetime
from django.forms import ValidationError
from core.models import Schedule, Patient


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['doctor', 'patient', 'date'] 
    

    def clean(self):
        doctor = self.cleaned_data.get('doctor')
        patient = self.cleaned_data.get('patient')
        date = self.cleaned_data.get('date')
        if datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc) > date:
            raise forms.ValidationError('Não pode fazer agendamento antes da data corrente!')
        if len(self.get_schedule_hour(doctor, patient, date)) > 0:
            raise forms.ValidationError(f'O agendamento para {patient} com o doutor: {doctor} já existe na data: {date}')
        
    def get_schedule_hour(self, doctor, patient, date):
        data_start = datetime.datetime(date.year, date.month, date.day, date.hour, 0)
        data_end = datetime.datetime(date.year, date.month, date.day, date.hour, 59)
        return Schedule.objects.filter(date__range=(data_start, data_end), doctor=doctor, patient=patient)

class PatientForms(forms.ModelForm):
    
    class Meta:
        model = Patient
        fields = [
            'full_name',
            'observation'
        ]