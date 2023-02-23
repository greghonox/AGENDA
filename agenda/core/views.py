from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse, JsonResponse
from django.contrib import messages
from django.conf import settings

from .models import Patient
from core.helper import PatientHandler
from core.forms import PatientForms

def index(request):
    return render(request, 'index.html')

@permission_required('core.add_patient')
def register_patient(request):
    handler = PatientHandler(request)
    data = {'form': handler.get_form()}
    if request.method == 'POST':
        if handler.execute():
            messages.success(request, 'Registrado Paciente com sucesso!!!')
        return redirect(to='register_patient')
    return render(request, 'register_patient.html', data)


@permission_required('core.add_patient')
def query_patient(request):
    patients = Patient.objects.all()
    return render(request, 'query_patient.html', {'patients': patients})
    

@permission_required('core.remove_patient')
def remove_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    patient.delete()
    messages.success(request, f'Removendo o {patient.full_name.title()} ({id}) com sucesso')
    return redirect(to='query_patient')

@permission_required('core.change_patient')
def change_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    data = {'form': PatientForms(instance=patient)}
    if request.method == 'POST':
        form = PatientForms(data=request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registrado Paciente com sucesso!!!')
            return redirect(to='query_patient')
    return render(request, 'register_patient.html', data)


def register_doctor(request):
    ...

def query_doctor(request):
    ...

def change_doctor(request):
    ...

def remove_doctor(request):
    ...

def register_scheduler(request):
    ...

def query_scheduler(request):
    ...

def change_scheduler(request):
    ...

def remove_scheduler(request):
    ...
