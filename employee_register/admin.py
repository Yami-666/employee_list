from django.contrib import admin

from .models import Employee, Passport, Unit, Statement, Position


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass

@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    pass
 
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    pass

@admin.register(Statement)
class StatementAdmin(admin.ModelAdmin):
    pass

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass

