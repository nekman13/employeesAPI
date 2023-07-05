from django.urls import path, include
from rest_framework.routers import DefaultRouter

from employees_api.views import ListCreateEmployeesAPIView, EmployeeUpdateAPIView, EmployeeDeleteAPIView

app_name = "employees_api"

# router = DefaultRouter()
# router.register(r"employee", EmployeeViewSet, basename="employee")


urlpatterns = [
    path("employee/", ListCreateEmployeesAPIView.as_view()),
    path("employee_update/<int:pk>/", EmployeeUpdateAPIView.as_view()),
    path("employee/<int:pk>/", EmployeeDeleteAPIView.as_view()),
    # path("", include(router.urls)),
]
