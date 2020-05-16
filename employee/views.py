from django.shortcuts import render, redirect

# Create your views here.
def employee_all(request):
    return render(request, 'employee/employee_list.html')