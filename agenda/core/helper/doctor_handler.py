from core.forms import DoctorForms


class DoctorHandler:
    def __init__(self, request):
        self.request = request
        
    def execute(self):
        form = DoctorForms(data=self.request.POST)
        if form.is_valid():
            form.save()
            return True
        return False

    @staticmethod
    def get_form():
        return DoctorForms()