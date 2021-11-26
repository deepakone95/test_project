from django.db.models.query_utils import Q
from django.shortcuts import render
from .models import Employee,Subject

# Create your views here.

def get_employee(request):
    emplaoyee = Employee.objects.all()
    query = Subject.objects.filter(employee_id=3).filter(Q(sname='hindi'))
    return render(request,'demo.html',{'query':query,'employee':emplaoyee})