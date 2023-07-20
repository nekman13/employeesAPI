from django.urls import include, path
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from employees_api.views import (
    EmployeeDeleteAPIView,
    EmployeeUpdateAPIView,
    ListCreateEmployeesAPIView,
)

app_name = "employees_api"

# router = DefaultRouter()
# router.register(r"employee", EmployeeViewSet, basename="employee")

schema_view = get_schema_view(
    openapi.Info(
        title="School Management System API",
        default_version='v1',
        description="API Documentation for School management System",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path("employee/", ListCreateEmployeesAPIView.as_view()),
    path("employee/<int:pk>/", EmployeeDeleteAPIView.as_view()),
    path("doc/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path("", include(router.urls)),
]
