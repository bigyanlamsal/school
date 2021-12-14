from django import forms
from .models import Notice_info, Vacancy_info, Carousel_info

class NoticesForm(forms.ModelForm):
    class Meta:
        model = Notice_info
        fields= ['title', 'detail', 'passport', 'date']

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy_info
        fields= ['subject', 'level', 'image_vacancy', 'date', 'end_date']

class CarouselForm(forms.ModelForm):
    class Meta:
        model = Carousel_info
        fields= ['image_name', 'image_carousel']