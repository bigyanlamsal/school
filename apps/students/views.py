import csv

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import widgets
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required

from apps.finance.models import Invoice

from .models import Student, StudentBulkUpload, Notice_info, Vacancy_info, Carousel_info , Administration_info
from basic.models import Admission_Student

from .form import NoticesForm, VacancyForm, CarouselForm, AdministrationForm
from django.shortcuts import render, redirect
from .filters import StudentFilter


class AdmissionListView(LoginRequiredMixin, ListView):
    context_object_name = 'obj'
    model = Admission_Student
    template_name = "students/admission_list.html"


class StudentListView(LoginRequiredMixin, ListView):
    context_object_name = 'obj'
    model = Student
    template_name = "students/student_list.html"
    #def get_queryset(self):
        #qs = self.model.objects.all()
        #student_filtered_list = OrderFilter(self.request.GET, queryset = qs)
        #return student_filtered_list.qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = StudentFilter(self.request.GET, queryset = self.get_queryset()) 
        return context
    

class AdmissionDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = "students/admission_detail.html"

    def get_context_data(self, **kwargs):
        context = super(AdmissionDetailView, self).get_context_data(**kwargs)
        
        return context

class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = "students/student_detail.html"

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        context["payments"] = Invoice.objects.filter(student=self.object)
        return context


class StudentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Student
    fields = "__all__"
    success_message = "New student successfully added."

    def get_form(self):
        """add date picker in forms"""
        form = super(StudentCreateView, self).get_form()
        form.fields["date_of_birth"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 2})
        form.fields["others"].widget = widgets.Textarea(attrs={"rows": 2})
        return form


class StudentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Student
    fields = "__all__"
    success_message = "Record successfully updated."

    def get_form(self):
        """add date picker in forms"""
        form = super(StudentUpdateView, self).get_form()
        form.fields["date_of_birth"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["date_of_admission"].widget = widgets.DateInput(
            attrs={"type": "date"}
        )
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 2})
        form.fields["others"].widget = widgets.Textarea(attrs={"rows": 2})
        # form.fields['passport'].widget = widgets.FileInput()
        return form


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy("student-list")

class AdmissionDeleteView(LoginRequiredMixin, DeleteView):
    model = Admission_Student
    success_url = reverse_lazy("admission-list")


class StudentBulkUploadView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = StudentBulkUpload
    template_name = "students/students_upload.html"
    fields = ["csv_file"]
    success_url = "/student/list"
    success_message = "Successfully uploaded students"


class DownloadCSVViewdownloadcsv(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="student_template.csv"'

        writer = csv.writer(response)
        writer.writerow(
            [
                "registration_number",
                "surname",
                "firstname",
                "other_names",
                "gender",
                "parent_number",
                "address",
                "current_class",
            ]
        )

        return response

@login_required
def show_notice(request):
    form = NoticesForm()
    return render(request, 'students/notice_publish.html', {'form': form})

@login_required
def show_vacancy(request):
    form = VacancyForm()
    return render(request, 'students/vacancy_publish.html', {'form': form})

@login_required
def show_carousel(request):
    form = CarouselForm()
    return render(request, 'students/carousel_publish.html', {'form': form})   

@login_required
def show_notice(request):
    form = NoticesForm()
    return render(request, 'students/notice_publish.html', {'form': form})

@login_required
def get_notice(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form_data = NoticesForm(request.POST, request.FILES)
        # check whether it's valid:
        if form_data.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            messages.success(request, 'Successfully published')
            form_data.save()
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NoticesForm()
    return redirect(show_notice)    

@login_required
def list_notice(request):
    object_list = Notice_info.objects.all()
    return render(request, 'students/notice_list.html', {'object_list': object_list})

@login_required
def update_notice(request, pk):
    if request.method == 'POST':
        pi = Notice_info.objects.get(id=pk)
        fm = NoticesForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.info(request, 'Successfully posted notice')
    else:
        pi = Notice_info.objects.get(id=pk)
        fm = NoticesForm(instance=pi)
    return render(request, 'students/notice_update.html', {'form': fm })

@login_required
def delete_notice(request, pk):
    if request.method == 'POST':
        pi = Notice_info.objects.get(id=pk)
        pi.delete()
        messages.error(request, 'Successfully deleted notice')
    return redirect(list_notice)    

@login_required
def list_vacancy(request):
    object_list = Vacancy_info.objects.all()
    return render(request, 'students/vacancy_list.html', {'object_list': object_list})
    
@login_required
def update_vacancy(request, pk):
    if request.method == 'POST':
        pi = Vacancy_info.objects.get(id=pk)
        fm = VacancyForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.info(request, 'Successfully posted vacancy')
    else:
        pi = Vacancy_info.objects.get(id=pk)
        fm = VacancyForm(instance=pi)
    return render(request, 'students/vacancy_update.html', {'form': fm })

@login_required
def delete_vacancy(request, pk):
    if request.method == 'POST':
        pi = Vacancy_info.objects.get(id=pk)
        pi.delete()
        messages.error(request, 'Successfully deleted vacancy')
    return redirect(list_vacancy)
  

@login_required
def show_vacancy(request):
    form = VacancyForm()
    return render(request, 'students/vacancy_publish.html', {'form': form})

@login_required
def list_gallery(request):
    object_list = Carousel_info.objects.all()
    return render(request, 'students/gallery_list.html', {'object_list': object_list})

@login_required
def show_carousel(request):
    form = CarouselForm()
    return render(request, 'students/carousel_publish.html', {'form': form})  

@login_required
def delete_gallery(request, pk):
    if request.method == 'POST':
        pi = Carousel_info.objects.get(id=pk)
        pi.delete()
        messages.error(request, 'Successfully deleted notice')
    return redirect(list_gallery)  



def get_vacancy(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form_data = VacancyForm(request.POST, request.FILES)
        # check whether it's valid:
        if form_data.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            messages.success(request, 'Successfully posted')
            form_data.save()
    # if a GET (or any other method) we'll create a blank form
    else:
        form = VacancyForm()
    return redirect(show_vacancy)

def get_carousel(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form_data = CarouselForm(request.POST, request.FILES)
        # check whether it's valid:
        if form_data.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            messages.success(request, 'Successfully posted carousel')
            form_data.save()
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CarouselForm()
    return redirect(show_carousel)

@login_required
def show_administration(request):
    form = AdministrationForm()
    return render(request, 'students/administration_publish.html', {'form': form})

@login_required
def get_administration(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form_data = AdministrationForm(request.POST, request.FILES)
        # check whether it's valid:
        if form_data.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            messages.success(request, 'Successfully added')
            form_data.save()
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AdministrationForm()
    return redirect(show_administration)    

@login_required
def list_administration(request):
    object_list = Administration_info.objects.all()
    return render(request, 'students/administration_list.html', {'object_list': object_list})

@login_required
def update_administration(request, pk):
    if request.method == 'POST':
        pi = Administration_info.objects.get(id=pk)
        fm = AdministrationForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.info(request, 'Successfully updated administration')
    else:
        pi = Administration_info.objects.get(id=pk)
        fm = AdministrationForm(instance=pi)
    return render(request, 'students/administration_update.html', {'form': fm })

@login_required
def delete_administration(request, pk):
    if request.method == 'POST':
        pi = Administration_info.objects.get(id=pk)
        pi.delete()
        messages.error(request, 'Successfully deleted administrative staff')
    return redirect(list_administration)    
