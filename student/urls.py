from django.urls import path
from .views import StudentList, StudentDetail, student_login, StudentRolesAppliedList, StudentRolesAppliedDetail, StudentApplicationList, StudentRolesAppliedList1, StudentInternshipList, StudentInternshipDetail, StudentInternshipList1, StudentList1, fetch_applied_status, fetch_internship_status, StudentInternshipsList1, StudentInternshipsList, StudentInternshipsDetail, StudentNotificationList, StudentNotificationDetail, StudentCompanyRoleNotification, ManagerStudentInternshipsList, StudentAssessmentList, StudentAssessmentDetail, StudentAssessmentList1, ManagerStudentInternshipsList1, ManagerStudentApplicationsList1


urlpatterns = [
    path('', StudentList.as_view()),
    path('studentView/', StudentList1.as_view()),
    path('<str:pk>', StudentDetail.as_view()),
    path('student-login/', student_login),
    path('student-roles-applied/', StudentRolesAppliedList.as_view()),
    path('student-roles-applied1/', StudentRolesAppliedList1.as_view()),
    path('student-roles-applied/<str:pk>', StudentRolesAppliedDetail.as_view()),
    path('studentapplication-list/<str:student_id>/', StudentApplicationList.as_view()),
    path('studentinternship-list/<str:student_id>/', StudentInternshipList1.as_view()),
    path('studentinternships-list/<str:student_id>/', StudentInternshipsList1.as_view()),
    path('managerstudentinternships-list/<str:company>/', ManagerStudentInternshipsList.as_view()),
    path('managerstudentinternships-list1/<str:company>/', ManagerStudentInternshipsList1.as_view()),
    path('student-applied-internships/', StudentInternshipList.as_view()),
    path('student-applied-internships/<str:pk>', StudentInternshipDetail.as_view()),
    path('studentinternships/', StudentInternshipsList.as_view()),
    path('studentinternships/<str:pk>', StudentInternshipsDetail.as_view()),
    path('fetch-applied-status/<str:student_id>/<str:role_id>', fetch_applied_status),
    path('fetch-internship-status/<str:student_id>/<str:role_id>', fetch_internship_status),

    path('student-company-notification/', StudentNotificationList.as_view()),
    path('student-company-notification/<str:pk>/', StudentNotificationDetail.as_view()),
    path('student-company-notification-list/<str:student_id>/', StudentCompanyRoleNotification.as_view()),

    path('managerstudentapplications-list/<str:company>/', ManagerStudentApplicationsList1.as_view()),

    path('student-assessment/', StudentAssessmentList.as_view()),
    path('student-assessment-list/', StudentAssessmentList1.as_view()),
    path('student-assessment/<str:pk>', StudentAssessmentDetail.as_view()),
]