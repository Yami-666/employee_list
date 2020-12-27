from django.forms import ModelForm
from .models import Employee, Passport, Statement
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'


class PassportForm(ModelForm):

    class Meta:
        model = Passport
        fields = ['fullname', 'serial_number', 'address', 'issed', 'code_subdivision', 'date_of_issed']
        widgets = {'date_of_issed' : DateInput()}


class EmployeeForm(ModelForm):

    class Meta:
        model = Employee
        fields = ['url_photo', 'phone', 'position', 'unit']


class StatementForm(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ['date_work', 'isAttended', 'salary']
        widgets = {'date_work' : DateInput()}

    
