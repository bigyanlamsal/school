from django import forms
from .models import Notice_info, Vacancy_info, Carousel_info , Administration_info

class NoticesForm(forms.ModelForm):
    class Meta:
        model = Notice_info
        fields= ['title', 'detail', 'passport', 'date']

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy_info
        fields= ['subject', 'level', 'image_vacancy', 'date', 'end_date']

class AdministrationForm(forms.ModelForm):
    class Meta:
        model = Administration_info
        fields= ['name', 'position', 'image_profile', 'description']        

class CarouselForm(forms.ModelForm):
    class Meta:
        model = Carousel_info
        fields= ['image_name', 'image_carousel']