import django_filters
from .models import *

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['firstname','surname','gender','current_class']
        {
            'firstname' : ['icontains'],
            'surname' : ['icontains'],
            'gendername' : ['icontains'],
            'current_class' : ['icontains'],
        }