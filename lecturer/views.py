from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics, permissions
from .models import Supervisor, SupervisorNotification
from .serializers import SupervisorSerializer, SupervisorNotificationSerializer, SupervisorNotificationSerializer1
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class SupervisorList(generics.ListCreateAPIView):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer
    # permission_classes = [permissions.IsAuthenticated]

class SupervisorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer
    # permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
def supervisor_login(request):
    username=request.POST['username']
    password=request.POST['password']
    try:
        supervisorData=Supervisor.objects.get(staff_id=username,password=password)
    except Supervisor.DoesNotExist:
        supervisorData=None
    if supervisorData:
        return JsonResponse({'bool':True, 'staff_id': supervisorData.staff_id, 'supervisor_name': supervisorData.last_name+" "+supervisorData.other_names})
    else:
        return JsonResponse({'bool':False})

class SupervisorNotificationList(generics.ListCreateAPIView):
    queryset = SupervisorNotification.objects.all().order_by('-id')
    serializer_class = SupervisorNotificationSerializer
    # permission_classes = [permissions.IsAuthenticated]

class SupervisorNotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SupervisorNotification.objects.all().order_by('-id')
    serializer_class = SupervisorNotificationSerializer
    # permission_classes = [permissions.IsAuthenticated]

# class SupervisorCompanyRoleNotification(generics.ListAPIView):
#     serializer_class = SupervisorNotificationSerializer1

#     def get_queryset(self):
#         staff_id=self.kwargs['staff_id']
#         supervisor=Supervisor.objects.get(pk=staff_id)
#         return SupervisorNotification.objects.filter(supervisor=supervisor).order_by('-id')