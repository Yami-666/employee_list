from django.forms import ModelForm
from .models import Employee, Passport, Statement

class PassportForm(ModelForm):

    class Meta:
        model = Passport
        fields = ['fullname', 'serial_number', 'address', 'issed', 'code_subdivision', 'date_of_issed']



class EmployeeForm(ModelForm):

    class Meta:
        model = Employee
        fields = ['url_photo', 'phone', 'position', 'unit']


class StatementForm(ModelForm):

    class Meta:
        model = Statement
        fields = ['date_work', 'isAttended', 'salary']

