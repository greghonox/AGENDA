from core.forms import ScheduleForms
from django.contrib import messages


class SchedulerHandler:
    def __init__(self, request):
        self.request = request
        
    def execute(self):
        form = ScheduleForms(data=self.request.POST)
        if form.is_valid():
            form.save()
            return True
        messages.error(self.request, form.errors.as_data()['__all__'][0].messages[0])
        return False


    @staticmethod
    def get_form():
        return ScheduleForms()
