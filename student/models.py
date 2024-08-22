from django.db import models
# from manager.models import RoleDetail

# Create your models here.
class Level(models.Model):
    level = models.CharField(max_length=10)

    def __str__(self):
        return self.level
    
class Programme(models.Model):
    programme = models.CharField(max_length=50)
    
    def __str__(self):
        return self.programme

    
class Student(models.Model):
    student_id = models.CharField(max_length=10, null=False, primary_key=True)
    password = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=150, null=False)
    other_names = models.CharField(max_length=150)
    email = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.CharField(max_length=150, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)
    level = models.ForeignKey(Level, on_delete=models.DO_NOTHING, null=True, blank=True)
    programme = models.ForeignKey(Programme, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.student_id

    
class StudentRolesApplied(models.Model):
    statusType = {
        "Accepted": "Accepted",
        "Rejected": "Rejected",
    }

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    role = models.ForeignKey('manager.RoleDetail', on_delete=models.CASCADE, related_name='student_roles_applied')
    applicationFile = models.FileField(null=True)
    applicationDate = models.DateField(auto_now_add=True, null=True)
    approval = models.CharField(blank=True, max_length=8, choices=statusType)
    class Meta:
        verbose_name_plural = "Student Roles Applied"

    def __str__(self):
        return self.student.student_id + " - " + self.role.company.companyName + " - " + self.role.role
    
class StudentAppliedInternship(models.Model):
    statusType = {
        "Accepted": "Accepted",
        "Rejected": "Rejected",
    }

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    role = models.ForeignKey('manager.RoleDetail', on_delete=models.CASCADE, related_name='student_accepted_roles')
    approval = models.CharField(blank=True, max_length=12, choices=statusType)
    smallInfo = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_data = models.DateField(null=True, blank=True)
    optionalFile = models.FileField(null=True)

    class Meta:
        verbose_name_plural = "Student Applied Internships"

    def __str__(self):
        return self.student.student_id + " - " + self.role.company.companyName + " - " + self.role.role
    
class StudentInternships(models.Model):
    offerType = {
        "Accepted": "Accepted",
        "Declined": "Declined",
    }

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    role = models.ForeignKey('manager.RoleDetail', on_delete=models.CASCADE, related_name='student_internships')
    company = models.ForeignKey('manager.Manager', on_delete=models.CASCADE, null=True)
    offer = models.CharField(blank=True, max_length=12, choices=offerType)

    class Meta:
        verbose_name_plural = "Student Internships"

    def __str__(self):
        return self.student.student_id + " - " + self.role.company.companyName + " - " + self.role.role
    
class StudentNotification(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    notText = models.TextField()

class StudentAssessment(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)
    # role = models.ForeignKey('manager.RoleDetail', on_delete=models.CASCADE)
    company = models.ForeignKey('manager.Manager', on_delete=models.CASCADE)
    email = models.CharField(max_length=150)
    durationOfInternship = models.CharField(max_length=150, null=True, blank=True)
    qualityOfWork = models.CharField(max_length=150)
    abilityToWork = models.CharField(max_length=150)
    initiativeAndCreativity = models.CharField(max_length=150)
    characterTraits = models.CharField(max_length=150)
    dependabilty = models.CharField(max_length=150)
    attendanceAndPunctuality = models.CharField(max_length=150)
    organizationalFit = models.CharField(max_length=150)
    responseToSupervision = models.CharField(max_length=150)
    suggestionsForImprovement = models.TextField(null=True, blank=True)
    nameOfSupervisor = models.CharField(max_length=150)
    positionOfSupervisor = models.CharField(max_length=150, null=True, blank=True)
    supervisorEmail = models.CharField(max_length=150, null=True, blank=True)
    supervisorContact = models.CharField(max_length=150, null=True, blank=True)