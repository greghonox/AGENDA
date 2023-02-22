from django.db import models

special_choice = (
    (0, 'Cirurgião plástico'),
    (1, 'Psiquiatra'),
    (2, 'Pediatra'),
    (3, 'Neurologista'),
    (4, 'Oncologista'),
    (5, 'Ginecologista'),
    (6, 'Homeopata'),
    (7, 'Alergista'),
    (8, 'Nutricionista'),
    (9, 'Pneumologista'),
    (10, 'Dermatologista'),
    (11, 'Geriatra'),
    (12, 'Neurocirurgião'),
    (13, 'Angiologista'),
    (14, 'Urologista'),
    (15, 'Psicólogo'),
    (16, 'Cardiologista'),
    (17, 'Acupunturista'),
    (18, 'Neuropsicólogo'),
    (19, 'RPG'),
    (20, 'Ortopedista e Traumatologista'),
)

class Doctor(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Nome Completo', null=True)
    observation = models.CharField(max_length=255, verbose_name='Observação', null=False)
    special = models.CharField(choices=special_choice, verbose_name='Especialidade médica', null=True)

class Patient(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Nome Completo', null=True)
    observation = models.CharField(max_length=255, verbose_name='Observação', null=False)
    

class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, verbose_name='Doutor', on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, verbose_name='Paciente', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(verbose_name='Data e Hora', null=True)
    

    class Meta:
        unique_together = (('Doctor', 'Patient', 'date'),)