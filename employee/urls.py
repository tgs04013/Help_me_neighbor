from django.urls import path

from .views import *

app_name = 'employee'

urlpatterns = [
    path('', employee_all, name='employee_all'),
]