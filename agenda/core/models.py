from django.db import models

special_choice = (
    ('cp', 'Cirurgião plástico'),
    ('ps', 'Psiquiatra'),
    ('pd', 'Pediatra'),
    ('ne', 'Neurologista'),
    ('on', 'Oncologista'),
    ('gi', 'Ginecologista'),
    ('ho', 'Homeopata'),
    ('al', 'Alergista'),
    ('nu', 'Nutricionista'),
    ('pn', 'Pneumologista'),
    ('de', 'Dermatologista'),
    ('ge', 'Geriatra'),
    ('nr', 'Neurocirurgião'),
    ('an', 'Angiologista'),
    ('ur', 'Urologista'),
    ('pi', 'Psicólogo'),
    ('ca', 'Cardiologista'),
    ('ac', 'Acupunturista'),
    ('nu', 'Neuropsicólogo'),
    ('rp', 'RPG'),
    ('ot', 'Ortopedista e Traumatologista'),
)

class Doctor(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Nome Completo', blank=False, error_messages={'required': 'Por favor insira um nome valido'})
    observation = models.CharField(max_length=255, verbose_name='Observação', blank=True, default='')
    special = models.CharField(max_length=50, choices=special_choice, verbose_name='Especialidade médica', blank=False)
    
    def __str__(self):
        return f'{self.full_name} {self.id}'

class Patient(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Nome Completo', blank=False, error_messages={'required': 'Por favor insira um nome valido'})
    observation = models.CharField(max_length=255, verbose_name='Observação', blank=True, default='')
    
    def __str__(self):
        return f'{self.full_name}'
    

class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, verbose_name='Doutor', on_delete=models.CASCADE, blank=False)
    patient = models.ForeignKey(Patient, verbose_name='Paciente', on_delete=models.CASCADE, blank=False)
    date = models.DateTimeField(verbose_name='Data e Hora', blank=False)
    

    class Meta:
        unique_together = (('doctor', 'patient', 'date'),)
        

    def __str__(self):
        return f'{self.doctor} {self.patient} {self.date}'
            