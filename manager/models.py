from django.db import models

# Create your models here.

class Manager(models.Model):
    
    status = {
        "Pending" : "Pending",
        "Verified" : "Verified",
    }

    companyName = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)
    ceo = models.CharField(max_length=100,)
    location = models.CharField(max_length=100)
    durationOfExistence = models.CharField(max_length=100)
    briefInfo = models.TextField()
    contractStatus = models.CharField(blank=True, max_length=8, choices=status)
    reportStatus = models.CharField(blank=True, max_length=8, choices=status)

    def __str__(self):
        return self.companyName

class RoleDetail(models.Model):
    company = models.ForeignKey(Manager, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, null=False)
    numberOfInterns = models.IntegerField(null=False)
    deadline = models.DateField(null=True)
    moreInfo = models.TextField(null=True)

    def __str__(self):
        return self.company.companyName + " - " + self.role