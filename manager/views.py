from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, permissions
from .serializers import ManagerSerializer, RoleDetailSerializer
from .models import Manager, RoleDetail
# Create your views here.

class ManagerList(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    # permission_classes = [permissions.IsAuthenticated]

class ManagerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    # permission_classes = [permissions.IsAuthenticated]

class RoleDetailList(generics.ListCreateAPIView):
    queryset = RoleDetail.objects.all()
    serializer_class = RoleDetailSerializer
    # permission_classes = [permissions.IsAuthenticated]

class RoleDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoleDetail.objects.all()
    serializer_class = RoleDetailSerializer
    # permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
def manager_login(request):
    username=request.POST['username']
    password=request.POST['password']
    try:
        managerData=Manager.objects.get(email=username,password=password)
    except Manager.DoesNotExist:
        managerData=None
    if managerData:
        return JsonResponse({'bool':True, 'manager_id': managerData.id, 'company_name': managerData.companyName})
    else:
        return JsonResponse({'bool':False})
    
class CompanyRolesList(generics.ListAPIView):
    serializer_class = RoleDetailSerializer

    def get_queryset(self):
        company_id=self.kwargs['manager_id']
        company=Manager.objects.get(pk=company_id)
        return RoleDetail.objects.filter(company=company)