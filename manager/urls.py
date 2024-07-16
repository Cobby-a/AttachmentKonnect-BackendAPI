from django.urls import path
from .views import ManagerList, ManagerDetail, RoleDetailList, RoleDetailDetail, manager_login

urlpatterns = [
    path('', ManagerList.as_view()),
    path('<str:pk>/', ManagerDetail.as_view()),
    path('manager-login', manager_login),
    path('roles', RoleDetailList.as_view()),
    path('roles/<str:pk>/', RoleDetailDetail.as_view())
]