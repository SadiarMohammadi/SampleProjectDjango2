from django.shortcuts import render, redirect

from .forms import EmployeeForm
from .models import *


# Create your views here.
def show(request):
    employees = Employee.objects.all()
    return render(request, "employee/show.html", {'employees': employees})


def emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'employee/index.html', {'form': form})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'employee/edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, "employee/edit.html", {'employee': employee})
