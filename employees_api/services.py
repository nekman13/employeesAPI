from django.forms import model_to_dict
from rest_framework.response import Response

from employees_api.models import Employee


def create_or_update(request):
    flag = False
    for employee in Employee.objects.all().values(
            "pk", "first_name", "last_name", "hire_date"
    ):
        if (
                request.data.get("first_name") == employee.get("first_name")
                and request.data.get("last_name") == employee.get("last_name")
                and request.data.get("hire_date") == employee.get("hire_date")
        ):
            flag = True
            pk = employee.get("pk")
            break
    input_employee_data = (
        request.data.get("first_name"),
        request.data.get("last_name"),
        request.data.get("department"),
        request.data.get("salary"),
        request.data.get("hire_date"),
    )
    if not flag:
        new_employee = Employee.objects.create(
            first_name=input_employee_data[0],
            last_name=input_employee_data[1],
            department=input_employee_data[2],
            salary=input_employee_data[3],
            hire_date=input_employee_data[4],
        )

        return Response(model_to_dict(new_employee))

    else:
        modify_employee = Employee.objects.get(pk=pk)
        (
            modify_employee.first_name,
            modify_employee.last_name,
            modify_employee.department,
            modify_employee.salary,
            modify_employee.hire_date,
        ) = input_employee_data
        modify_employee.save()

        return Response(model_to_dict(modify_employee))
