from core.forms import PatientForms

class PatientHandler:
    def __init__(self, request):
        self.request = request
        
    def execute(self, patient=None):
        form = PatientForms(data=self.request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return True
        return False

    @staticmethod
    def get_form():
        return PatientForms()
