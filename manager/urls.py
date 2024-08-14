from django.urls import path
from .views import ManagerList, ManagerDetail, RoleDetailList, RoleDetailDetail, manager_login, CompanyRolesList, RoleDetailOnlyList, RoleDetailOnlyDetail, ManagerNotificationList, ManagerNotificationDetail, CompanyStudentRoleNotification

urlpatterns = [
    path('', ManagerList.as_view()),
    path('<str:pk>', ManagerDetail.as_view()),
    path('manager-login/', manager_login),
    path('roles/', RoleDetailList.as_view()),
    path('rolesView/', RoleDetailOnlyList.as_view()),
    path('roles/<str:pk>/', RoleDetailDetail.as_view()),
    path('rolesView/<str:pk>/', RoleDetailOnlyDetail.as_view()),
    path('companyroles-list/<int:manager_id>/', CompanyRolesList.as_view()),
    path('company-student-notification/', ManagerNotificationList.as_view()),
    path('company-student-notification/<str:pk>/', ManagerNotificationDetail.as_view()),
    path('company-student-notification-list/<int:manager_id>/', CompanyStudentRoleNotification.as_view()),
]