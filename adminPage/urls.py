from django.urls import path
from .views import AdminUsersList, AdminUserDetail, adminUser_login

urlpatterns = [
    path('', AdminUsersList.as_view()),
    path('<str:pk>', AdminUserDetail.as_view()),
    path('admin-login/', adminUser_login),
]