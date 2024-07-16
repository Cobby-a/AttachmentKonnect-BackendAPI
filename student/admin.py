from django.contrib import admin
from .models import Student, StudentRolesApplied

# Register your models here.

admin.site.register(Student)
admin.site.register(StudentRolesApplied)