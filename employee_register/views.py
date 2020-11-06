from django.shortcuts import render, redirect
from .forms import EmployeeForm, PassportForm, StatementForm
from .models import Employee, Passport, Statement


def get_employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, 'employee_register/employee_list.html', context)


def employee_form(request, id=0):
    if request.method == "GET":
        #При запросе пользователя отобразить пустые формы
        if id == 0:
            eForm = EmployeeForm
            pForm = PassportForm
        #При запросе существующей записи
        #Заполнить поля этой формой
        else:
            employee = Employee.objects.get(pk=id)
            pForm = PassportForm(instance=employee.passport)
            eForm = EmployeeForm(instance=employee)
        #Отправка форм в html
        return render(request, 'employee_register/employee_form.html', {'eForm': eForm, 'pForm': pForm})
    elif request.method == "POST":
        #При отправке пустой формой ничего не меняем
        if id == 0:
            pForm = PassportForm(request.POST)
            eForm = EmployeeForm(request.POST, files=request.FILES)
        #При отправке изменённой формы, мы пересоздаём её в модели   
        else:
            employee = Employee.objects.get(pk=id)
            pForm = PassportForm(request.POST, instance=employee.passport)
            eForm = EmployeeForm(request.POST, instance=employee,  files=request.FILES)
            
        #Проверка и сохранение форм
        if eForm.is_valid() and pForm.is_valid():
            pas = pForm.save()
            emp = eForm.save()
            emp.passport = pas
            emp.save()
        
        return redirect('/employee/list/')


def statement_form(request, id):
    if request.method == "GET":
        sForm = StatementForm
        return render(request, 'employee_register/statement_form.html', {'sForm': sForm})
    elif request.method == "POST":
        sForm = StatementForm(request.POST)
    if sForm.is_valid():
        employee = Employee.objects.get(pk=id)
        stat = sForm.save()
        stat.employee = employee
        stat.save()

        return redirect('/employee/list/')


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list/')


def get_passport(request, id):
    employee = Employee.objects.get(pk=id)
    passport = employee.passport
   
    return render(request, 'employee_register/employee_passport.html', {'passport': passport})


def get_statement_list(request, id):
    employee = Employee.objects.get(pk=id)
    statement = employee.statement_set.all()

    return render(request, 'employee_register/employee_statement.html', {'statement': statement, 'employee': employee})

