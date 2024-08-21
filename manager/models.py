from django.db import models
from student.models import StudentInternships
from django.core.mail import send_mail
# Create your models here.

class Manager(models.Model):
    
    status = {
        "Pending" : "Pending",
        "Verified" : "Verified",
    }

    companyName = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=True)
    ceo = models.CharField(max_length=100,)
    location = models.CharField(max_length=100)
    durationOfExistence = models.CharField(max_length=100)
    briefInfo = models.TextField()
    contractStatus = models.CharField(blank=True, max_length=8, choices=status)
    reportStatus = models.CharField(blank=True, max_length=8, choices=status)
    companyLogo = models.ImageField( null=True)
    companyCertificate = models.FileField(null = True)

    def __str__(self):
        return self.companyName

    def save(self, *args, **kwargs):
        send_mail(
            'Company Info',
            'Here is the message.',
            'attachmentkonnect@gmail.com',
            ['attachmentkonnect@gmail.com'],
            fail_silently=False,
            html_message=f'<p><strong>Company Name:</strong>{self.companyName}<p/><p><strong>Company Email:</strong>{self.email}<p/><p><strong>Company Location:</strong>{self.location}<p/><p><strong>Company Ceo:</strong>{self.ceo}<p/><p><strong>Company Duration of Existence:</strong>{self.durationOfExistence}<p/><p><strong>Brief Intel:</strong>{self.briefInfo}<p/><p><strong>Logo:</strong>{self.companyLogo}<p/><p><strong>Certificate:</strong>{self.companyCertificate}<p/>',
        )
        return super(Manager,self).save(*args, **kwargs)
    
class RoleDetail(models.Model):
    company = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='company_vacancies')
    role = models.CharField(max_length=100, null=False)
    numberOfInterns = models.IntegerField(null=False)
    deadline = models.DateField(null=True, blank=True)
    moreInfo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.company.companyName + " - " + self.role
    
    def total_accepted_students(self):
        total_accepted_students=StudentInternships.objects.filter(role=self, offer="Accepted").count()
        return total_accepted_students
    
class ManagerNotification(models.Model):
    company = models.ForeignKey(Manager, on_delete=models.CASCADE)
    role = models.ForeignKey(RoleDetail, on_delete=models.CASCADE)
    notText = models.TextField()