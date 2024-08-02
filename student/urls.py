from django.urls import path
from .views import StudentList, StudentDetail, student_login, StudentRolesAppliedList, StudentRolesAppliedDetail, StudentApplicationList, StudentRolesAppliedList1, StudentInternshipList, StudentInternshipDetail, StudentInternshipList1


urlpatterns = [
    path('', StudentList.as_view()),
    path('<str:pk>', StudentDetail.as_view()),
    path('student-login/', student_login),
    path('student-roles-applied/', StudentRolesAppliedList.as_view()),
    path('student-roles-applied1/', StudentRolesAppliedList1.as_view()),
    path('student-roles-applied/<str:pk>', StudentRolesAppliedDetail.as_view()),
    path('studentapplication-list/<str:student_id>/', StudentApplicationList.as_view()),
    path('studentinternship-list/<str:student_id>/', StudentInternshipList1.as_view()),
    path('student-internships/', StudentInternshipList.as_view()),
    path('student-internships/<str:pk>', StudentInternshipDetail.as_view()),
]