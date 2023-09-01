from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.generics import DestroyAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.viewsets import ViewSet

from employees_api.models import Employee
from employees_api.permissions import IsAdminOrReadOnly
from employees_api.serializers import EmployeesSerializer
from employees_api.services import create_or_update

from rest_framework.permissions import IsAuthenticated


# Create your views here.


class ListCreateEmployeesAPIView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer

    # permission_classes = (IsAdminOrReadOnly,)

    def post(self, request, *args, **kwargs):
        return create_or_update(request)


class EmployeeDeleteAPIView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer
    # permission_classes = (IsAdminOrReadOnly,)


class DepartmentAPIView(ListAPIView):
    serializer_class = 


class IndexView(TemplateView):
    template_name = "employees_api/index.html"
