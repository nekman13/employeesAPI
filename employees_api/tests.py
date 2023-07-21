from django.test import TestCase
from rest_framework.test import APITestCase, RequestsClient

from .models import Employee

# Create your tests here.


class MainPageTestCase(TestCase):
    """Класс тестов исходной страницы"""

    def test_view(self):
        response = self.client.get("http://127.0.0.1:8000/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "employees_api/index.html")


class EmployeeTestCase(APITestCase):
    """Класс тестов работы с сотрудниками"""

    fixtures = ["employee.json"]

    def setUp(self):
        self.data = {
            "first_name": "Тест_имя",
            "last_name": "Тест_фамилия",
            "department": "Тест_департамент",
            "salary": 10000,
            "hire_date": "2022-01-01",
            "tasks": [],
        }
        self.path = "http://127.0.0.1:8000/api/v1/employee/"

    def test_get_employee_list(self):
        response_get_all_employees = self.client.get(self.path)
        self.assertEqual(response_get_all_employees.status_code, 200)

    def test_post_employee(self):
        response_post_employee = self.client.post(
            path=self.path, data=self.data, format="json"
        )
        self.assertEqual(response_post_employee.status_code, 200)

    def test_delete_employee(self):
        pk = Employee.objects.last().pk
        response_delete_employee = self.client.delete(path=f"{self.path}{pk}/")
        self.assertEqual(response_delete_employee.status_code, 204)


class DocumentationTestCase(TestCase):
    """Класс тестов документации"""

    def test_view(self):
        response = self.client.get("https://127.0.0.1:8000/api/v1/doc/")
        self.assertEqual(response.status_code, 200)
