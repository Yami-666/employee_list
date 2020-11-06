from django.db import models


class Employee(models.Model):

    url_photo = models.ImageField(upload_to="employee-photo/", verbose_name="Фото сотрудника", null=True, blank=True)
    passport = models.OneToOneField('Passport', on_delete=models.CASCADE, default='', null=True)
    phone = models.CharField(max_length=25, verbose_name="Номер телефона", default='')
    position = models.ManyToManyField('Position')
    unit = models.ManyToManyField('Unit')

    def __str__(self):
        return str(self.id) + " " + str(self.passport.fullname)


class Passport(models.Model):

    fullname = models.CharField(max_length=50, verbose_name="ФИО")
    serial_number = models.CharField(max_length=10, verbose_name="Серия и номер")
    address = models.CharField(max_length=50, verbose_name="Адресс прописки")
    issed = models.CharField(max_length=255, verbose_name="Паспорт выдан")
    code_subdivision = models.CharField(max_length=25, verbose_name="Код-подразделения")
    date_of_issed = models.DateField()
    #file_passport_copy = models.FileField(upload_to='/uploads')


class Statement(models.Model):

    date_work = models.DateField(verbose_name="Дата")
    isAttended = models.BooleanField(default=True, verbose_name="Присутствовал?")
    salary = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Зарплата за текущий день")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.employee.passport.fullname)


class Position(models.Model):

    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Unit(models.Model):

    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
