from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, permissions
from .serializers import StudentSerializer, StudentRolesAppliedSerilaizer, StudentRolesAppliedSerilaizer1
from .models import Student, StudentRolesApplied
# Create your views here.

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = [permissions.IsAuthenticated]

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = [permissions.IsAuthenticated]

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
        return StudentRolesApplied.objects.filter(student=student)