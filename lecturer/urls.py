from django.urls import path
from .views import LecturerList, LecturerDetail

urlpatterns = [
    path("", LecturerList.as_view(), name="lecturers"),
    path("<str:pk>/", LecturerDetail.as_view(), name="lecturer_detail")
]