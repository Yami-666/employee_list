from django.urls import path, include
from django.conf.urls import url
from . import views



urlpatterns = [
    path('', views.employee_form, name='employee_insert'),
    path('<int:id>/', views.employee_form, name='employee_update'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    path('list/', views.get_employee_list, name='get_employee_list'),
    path('passport/<int:id>/', views.get_passport, name='get_passport'),
    path('<int:id>/statement/list', views.get_statement_list, name='get_statement_list'),
    path('<int:id>/statement/form', views.statement_form, name='statement_insert')
]

