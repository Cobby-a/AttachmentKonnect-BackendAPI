from django.shortcuts import render
from .models import AdminUser
from .serializers import AdminUserSerializer
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.


class AdminUsersList(generics.ListCreateAPIView):
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer

class AdminUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer

@csrf_exempt
def adminUser_login(request):
    username=request.POST['username']
    password=request.POST['password']
    try:
        adminUserData=AdminUser.objects.get(username=username,password=password)
    except AdminUser.DoesNotExist:
        adminUserData=None
    if adminUserData:
        return JsonResponse({'bool':True, 'admin_id': adminUserData.id, 'adminUsername': adminUserData.username})
    else:
        return JsonResponse({'bool':False})