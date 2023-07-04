from django.urls import path

from employees_api.views import ListEmployeesAPIView

app_name = "employees_api"

urlpatterns = [
    path("employees/", ListEmployeesAPIView.as_view())
]