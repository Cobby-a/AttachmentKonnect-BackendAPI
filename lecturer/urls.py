from django.urls import path
from .views import SupervisorList, SupervisorDetail, supervisor_login, SupervisorNotificationList, SupervisorNotificationDetail, SupervisorCompanyRoleNotification

urlpatterns = [
    path("", SupervisorList.as_view()),
    path("<str:pk>", SupervisorDetail.as_view()),
    path('supervisor-login/', supervisor_login),

    path('supervisor-company-notification/', SupervisorNotificationList.as_view()),
    path('supervisor-company-notification/<str:pk>/', SupervisorNotificationDetail.as_view()),
    path('supervisor-company-notification-list/<str:staff_id>/', SupervisorCompanyRoleNotification.as_view()),
]