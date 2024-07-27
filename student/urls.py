from django.urls import path
from .views import StudentList, StudentDetail, student_login, StudentRolesAppliedList, StudentRolesAppliedDetail, StudentApplicationList


urlpatterns = [
    path('', StudentList.as_view()),
    path('<str:pk>', StudentDetail.as_view()),
    path('student-login/', student_login),
    path('student-roles-applied/', StudentRolesAppliedList.as_view()),
    path('student-roles-applied/<str:pk>', StudentRolesAppliedDetail.as_view()),
    path('studentapplication-list/<str:student_id>/', StudentApplicationList.as_view()),
]