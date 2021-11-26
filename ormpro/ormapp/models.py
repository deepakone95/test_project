from django.db import models

# Create your models here.

class Employee(models.Model):
    eno = models.IntegerField(null= True)
    ename = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.ename

class Subject(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    sname = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f'{self.employee_id}----{self.sname}'


