from django.db import models
from manager.models import Manager, RoleDetail

# Create your models here.

class Student(models.Model):
    student_id = models.CharField(max_length=10, null=False, primary_key=True)
    password = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=150, null=False)
    other_names = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=150)

    def __str__(self):
        return self.student_id

class StudentRolesApplied(models.Model):
    statusType = {
        "Accepted": "Accepted",
        "Rejected": "Rejected",
    }

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    studentId = models.CharField(max_length=150)
    company = models.ForeignKey(Manager, on_delete=models.CASCADE)
    role = models.ForeignKey(RoleDetail, on_delete=models.CASCADE)
    status = models.CharField(blank=True, max_length=8, choices=statusType)
    approval = models.CharField(blank=True, max_length=8, choices=statusType)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name_plural = "Student Roles Applied"

    def __str__(self):
        return self.student.student_id + " - " + self.role.company.companyName + " - " + self.role.role