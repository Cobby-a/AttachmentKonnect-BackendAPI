from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, permissions
from .serializers import StudentSerializer, StudentRolesAppliedSerilaizer, StudentRolesAppliedSerilaizer1, StudentInternshipSerilaizer, StudentInternshipSerilaizer1, StudentSerializer1, StudentInternshipsSerilaizer, StudentInternshipsSerilaizer1, StudentNotificationSerializer, StudentNotificationSerializer1
from .models import Student, StudentRolesApplied, StudentAppliedInternship, StudentInternships, StudentNotification
# Create your views here.
from manager.models import RoleDetail
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 3

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all().order_by('student_id')
    serializer_class = StudentSerializer
    # permission_classes = [permissions.IsAuthenticated]

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = [permissions.IsAuthenticated]

class StudentList1(generics.ListAPIView):
    queryset = Student.objects.all().order_by('student_id')
    serializer_class = StudentSerializer1
    pagination_class = StandardResultsSetPagination

@csrf_exempt
def student_login(request):
    username=request.POST['username']
    password=request.POST['password']
    try:
        studentData=Student.objects.get(student_id=username,password=password)
    except Student.DoesNotExist:
        studentData=None
    if studentData:
        return JsonResponse({'bool':True, 'student_id': studentData.student_id, 'student_name': studentData.last_name+" "+studentData.other_names})
    else:
        return JsonResponse({'bool':False})

class StudentRolesAppliedList(generics.ListCreateAPIView):
    queryset = StudentRolesApplied.objects.all()
    serializer_class = StudentRolesAppliedSerilaizer

class StudentRolesAppliedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentRolesApplied.objects.all()
    serializer_class = StudentRolesAppliedSerilaizer

class StudentApplicationList(generics.ListAPIView):
    serializer_class = StudentRolesAppliedSerilaizer1

    def get_queryset(self):
        student_id=self.kwargs['student_id']
        student=Student.objects.get(pk=student_id)
        return StudentRolesApplied.objects.filter(student=student).order_by('-id')
    
class StudentInternshipList1(generics.ListAPIView):
    serializer_class = StudentInternshipSerilaizer1

    def get_queryset(self):
        student_id=self.kwargs['student_id']
        student=Student.objects.get(pk=student_id)
        return StudentAppliedInternship.objects.filter(student=student).order_by('-id')
    
class StudentInternshipsList1(generics.ListAPIView):
    serializer_class = StudentInternshipsSerilaizer1

    def get_queryset(self):
        student_id=self.kwargs['student_id']
        student=Student.objects.get(pk=student_id)
        return StudentInternships.objects.filter(student=student).order_by('-id')

class StudentRolesAppliedList1(generics.ListAPIView):
    queryset = StudentRolesApplied.objects.all().order_by('-id')
    serializer_class = StudentRolesAppliedSerilaizer1
    pagination_class = StandardResultsSetPagination

class StudentInternshipList(generics.ListCreateAPIView):
    queryset = StudentAppliedInternship.objects.all()
    serializer_class = StudentInternshipSerilaizer

class StudentInternshipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentAppliedInternship.objects.all()
    serializer_class = StudentInternshipSerilaizer

class StudentInternshipsList(generics.ListCreateAPIView):
    queryset = StudentInternships.objects.all()
    serializer_class = StudentInternshipsSerilaizer

class StudentInternshipsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentInternships.objects.all()
    serializer_class = StudentInternshipsSerilaizer

def fetch_applied_status(request, student_id, role_id):
    student = Student.objects.filter(student_id= student_id).first()
    role = RoleDetail.objects.filter(id=role_id).first()
    appliedStatus = StudentRolesApplied.objects.filter(student=student, role=role).count()
    internshipStatus = StudentAppliedInternship.objects.filter(student=student, role=role).count()
    internship = StudentInternships.objects.filter(student=student, role=role).count()
    if appliedStatus or internshipStatus or internship:
        return JsonResponse({'bool': True})
    else:
        return JsonResponse({'bool': False})
    
def fetch_internship_status(request, student_id, role_id):
    student = Student.objects.filter(student_id= student_id).first()
    role = RoleDetail.objects.filter(id=role_id).first()
    appliedStatus = StudentAppliedInternship.objects.filter(student=student, role=role).count()
    if appliedStatus:
        return JsonResponse({'bool': True})
    else:
        return JsonResponse({'bool': False})
    
class StudentNotificationList(generics.ListCreateAPIView):
    queryset = StudentNotification.objects.all().order_by('-id')
    serializer_class = StudentNotificationSerializer
    # permission_classes = [permissions.IsAuthenticated]

class StudentNotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentNotification.objects.all().order_by('-id')
    serializer_class = StudentNotificationSerializer
    # permission_classes = [permissions.IsAuthenticated]

class StudentCompanyRoleNotification(generics.ListAPIView):
    serializer_class = StudentNotificationSerializer1

    def get_queryset(self):
        student_id=self.kwargs['student_id']
        student=Student.objects.get(pk=student_id)
        return StudentNotification.objects.filter(student=student).order_by('-id')