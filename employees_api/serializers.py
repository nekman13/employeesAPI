from rest_framework import serializers

from employees_api.models import Employee


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
