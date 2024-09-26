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
    website = models.CharField(max_length=100, null=True)
    facebook = models.CharField(max_length=100, null=True)
    twitter = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
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
            html_message=f'<p><strong>Company Name:</strong>{self.companyName}<p/><p><strong>Company Email:</strong>{self.email}<p/><p><strong>Company Location:</strong>{self.location}<p/><p><strong>Company Ceo:</strong>{self.ceo}<p/><p><strong>Company Duration of Existence:</strong>{self.durationOfExistence}<p/><p><strong>Missions Visions and goals:</strong>{self.briefInfo}<p/><p><strong>Website</strong>{self.website}<p/><p><strong>Facebook</strong>{self.facebook}<p/><p><strong>Twitter</strong>{self.twitter}<p/><p><strong>Instagram</strong>{self.instagram}<p/><p><strong>Logo:</strong>{self.companyLogo}<p/><p><strong>Certificate:</strong>{self.companyCertificate}<p/>',
        )
        return super(Manager,self).save(*args, **kwargs)
    
class CompanyRegistered(models.Model):

    companyName = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.companyName

    def save(self, *args, **kwargs):
        send_mail(
            'Company Registration Approved - Access Your Account',
            'Here is the message.',
            'attachmentkonnect@gmail.com',
            [self.email],
            fail_silently=False,
            html_message=f'<p>Dear Manager,</p><p>This is an automated notification to inform you that your company has been successfully accepted into our system.</p><p>To access your account, please follow these steps:</p><ol><li>Go to our portal, https://attachment-konnect.vercel.app/portal and checkbox the manager</li><li>Log in using the following credentials <ul><li>Your email address: {self.email}</li><li>Temporal Password: attachmentkonnect</li></ul></li></ol><p>Upon your first login, you will be prompted to change your password. Once updated, you will have full access to the system.</p><p>Please note: This is an automated message; if you have any issues or need assistance, feel free to contact our support team via email.</p><p>Thank you, <br/>[AttachmentKonnect]</p>',
        )
        return super(CompanyRegistered,self).save(*args, **kwargs)
    
class ManagerProfileChange(models.Model):

    companyName = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    ceo = models.CharField(max_length=100,)
    location = models.CharField(max_length=100)
    durationOfExistence = models.CharField(max_length=100)
    briefInfo = models.TextField()
    website = models.CharField(max_length=100, null=True)
    facebook = models.CharField(max_length=100, null=True)
    twitter = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
    companyLogo = models.ImageField( null=True)

    def __str__(self):
        return self.companyName

    def save(self, *args, **kwargs):
        send_mail(
            f'Company {self.companyName} Change Info',
            'Here is the message.',
            'attachmentkonnect@gmail.com',
            ['attachmentkonnect@gmail.com'],
            fail_silently=False,
            html_message=f'<p><strong>Company Name:</strong>{self.companyName}<p/><p><strong>Company Email:</strong>{self.email}<p/><p><strong>Company Location:</strong>{self.location}<p/><p><strong>Company Ceo:</strong>{self.ceo}<p/><p><strong>Company Duration of Existence:</strong>{self.durationOfExistence}<p/><p><strong>Missions Visions and goals:</strong>{self.briefInfo}<p/><p><strong>Website</strong>{self.website}<p/><p><strong>Facebook</strong>{self.facebook}<p/><p><strong>Twitter</strong>{self.twitter}<p/><p><strong>Instagram</strong>{self.instagram}<p/><p><strong>Logo:</strong>{self.companyLogo}<p/>',
        )
        return super(ManagerProfileChange,self).save(*args, **kwargs)
    
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