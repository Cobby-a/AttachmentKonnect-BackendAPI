from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Lecture
from .serializers import LecturerSerializer

# Create your views here.

class LecturerList(generics.ListCreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LecturerSerializer
    permission_classes = [permissions.IsAuthenticated]

class LecturerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LecturerSerializer
    permission_classes = [permissions.IsAuthenticated]
