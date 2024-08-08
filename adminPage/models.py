from django.db import models

# Create your models here.


class AdminUser(models.Model):
    username = models.CharField(max_length=10, null=False, unique=True)
    password = models.CharField(max_length=150, null=False)