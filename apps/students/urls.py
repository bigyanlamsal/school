from django.urls import path
from . import views

from .views import (
    DownloadCSVViewdownloadcsv,
    StudentBulkUploadView,
    StudentCreateView,
    StudentDeleteView,
    StudentDetailView,
    StudentListView,
    StudentUpdateView,
    AdmissionListView,
    AdmissionDeleteView,
    AdmissionDetailView,
  
)

urlpatterns = [
    path("ad_list/", AdmissionListView.as_view(), name="admission-list"),
    path("list/", StudentListView.as_view(), name="student-list"),
    path("<int:pk>/", StudentDetailView.as_view(), name="student-detail"),
    path("admission_pk/<int:pk>/", AdmissionDetailView.as_view(), name="admission-detail"),
    path("create/", StudentCreateView.as_view(), name="student-create"),
    path("<int:pk>/update/", StudentUpdateView.as_view(), name="student-update"),
    path("delete/<int:pk>/", StudentDeleteView.as_view(), name="student-delete"),
    path("admission_pk/delete/<int:pk>/",AdmissionDeleteView.as_view(), name="admission-delete"),
    path("upload/", StudentBulkUploadView.as_view(), name="student-upload"),
    path("download-csv/", DownloadCSVViewdownloadcsv.as_view(), name="download-csv"),
    path("publish_in_notice/", views.show_notice, name="publish_in_notice"),
    path("notice_list/", views.list_notice, name="notice_list"),
    path("publish_in_vacancy/", views.show_vacancy, name="publish_in_vacancy"),
    path("notice_publish/", views.get_notice, name="get_notice"),
    path("vacancy_publish/", views.get_vacancy, name="get_vacancy"),
    path("publish_in_carousel/", views.show_carousel, name="publish_in_carousel"),
    path("carousel_publish/", views.get_carousel, name="get_carousel"),
    path(
        "notice_list/<int:pk>/update/",
        views.update_notice,
        name="update_notice",
    ),
    path(
        "notice_list/delete/<int:pk>/",
        views.delete_notice,
        name="delete_notice",
    ),


    
]
