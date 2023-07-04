from django.shortcuts import render
from rest_framework.generics import ListAPIView

from employees_api.models import Employee
from employees_api.serializers import EmployeesSerializer


# Create your views here.


class ListEmployeesAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer


