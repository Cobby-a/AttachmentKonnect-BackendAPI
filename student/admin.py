from django.contrib import admin
from .models import Student, StudentRolesApplied, Level, Programme

# Register your models here.

admin.site.register(Student)
admin.site.register(StudentRolesApplied)
admin.site.register(Level)
admin.site.register(Programme)