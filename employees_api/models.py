from django.contrib.postgres.fields import ArrayField
from django.db import models
from rest_framework import validators


class Employee(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    department = models.CharField(max_length=100, verbose_name="Департамент")
    salary = models.CharField(max_length=100, verbose_name="Заработная плата")
    hire_date = models.CharField(max_length=10, verbose_name="Дата приема")
    tasks = ArrayField(
        base_field=models.CharField(max_length=150),
        verbose_name="Задачи",
        blank=True,
        default=[],
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"
