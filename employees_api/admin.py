from django.contrib import admin

from employees_api.models import Employee, User

# Register your models here.

admin.site.register(Employee)
admin.site.register(User)
