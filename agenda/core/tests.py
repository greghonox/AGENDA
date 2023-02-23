from django.test import TestCase
from django.test import LiveServerTestCase


class TestRegisterQuery(LiveServerTestCase):
    def test_register_patient(self):
        self.assertTrue(True)

    def test_register_doctor(self):
        self.assertTrue(True)

    def test_register_schedule(self):
        self.assertTrue(True)                

    def test_query_patient(self):
        self.assertTrue(True)

    def test_query_doctor(self):
        self.assertTrue(True)

    def test_query_schedule(self):
        self.assertTrue(True)                        

class TestCases(LiveServerTestCase):
    def test_register_sheduler_with_register_query_should_error(self):
        self.assertFalse(False)   
     
        
class TestHelpersHandler(LiveServerTestCase):
    def test_scheduler_handler_with_register_sucess(self):
        self.assertTrue(True)       

    def test_scheduler_handler_with_register_error(self):
        self.assertFalse(False)

    def test_patient_handler_with_register_sucess(self):
        self.assertTrue(True)       

    def test_patient_handler_with_register_error(self):
        self.assertFalse(False)

    def test_doctor_handler_with_register_sucess(self):
        self.assertTrue(True)       

    def test_doctor_handler_with_register_error(self):
        self.assertFalse(False)                