from django.db import models

# Create your models here.

class Lecture(models.Model):
    staff_id = models.CharField(max_length=10, null=False, primary_key=True)
    password = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=150, null=False)
    other_names = models.CharField(max_length=150)

    def __str__(self):
        return self.staff_id