from django.contrib import admin
from .models import Student, StudentRolesApplied, Level, Programme, StudentAppliedInternship, StudentInternships, StudentAssessment, StudentNotification

# Register your models here.

admin.site.register(Student)
admin.site.register(StudentRolesApplied)
admin.site.register(Level)
admin.site.register(Programme)
# admin.site.register(StudentAppliedInternship)
# admin.site.register(StudentInternships)
# admin.site.register(StudentAssessment)
# admin.site.register(StudentNotification)