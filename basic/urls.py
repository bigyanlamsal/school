from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('admin_office/', views.admin_office, name='admin_office'),
    path('admission/', views.admission, name='admission'),
    path('admission_backend/', views.admission_backend, name='admission_backend'),
    path('admin_office_login/', views.admin_office_login, name='admin_office_login'),
    path('vacancy/', views.vacancy, name='vacancy'),
    path('gallery/', views.gallery, name='gallery'),
]