from django.urls import path
from .views import StudentList, StudentDetail, student_login


urlpatterns = [
    path('', StudentList.as_view()),
    path('<str:pk>', StudentDetail.as_view()),
    path('student-login/', student_login),
]