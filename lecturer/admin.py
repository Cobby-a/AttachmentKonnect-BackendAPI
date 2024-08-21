from django.contrib import admin
from .models import Supervisor, SupervisorNotification

# Register your models here.

admin.site.register(Supervisor)
admin.site.register(SupervisorNotification)