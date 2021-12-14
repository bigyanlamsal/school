from django.shortcuts import render, redirect, HttpResponse
from basic import models
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from apps.students.models import Notice_info, Vacancy_info , Carousel_info
# Create your views here.
def index(request):
    obj = Notice_info.objects.all()
    img = Carousel_info.objects.all()
    return render(request, "basic/index.html",{'obj': obj,'img':img})

def admin_office(request):
    return render(request, "basic/admin.html")

def admission(request):
    return render(request, "basic/admission.html")
    

def vacancy(request):
    obj = Vacancy_info.objects.all()
    return render(request, "basic/vacancy.html",{'obj':obj})

def admission_backend(request):
    if request.method == "POST":
        fname =  request.POST['firstName']
        lname = request.POST['lastName']
        fa_name = request.POST['fathersName']
        mo_name = request.POST['mothersName']
        class_name = request.POST['classNumber']
        mobile_num = request.POST['mob_number']
        email_ = request.POST['email']


        grade_values = request.POST['gradeValue']
        reviews_ = request.POST['subject']

        adm = models.Admission_Student(first_name=fname, last_name=lname, father_name=fa_name, mothers_name=mo_name, class_numbers=class_name, mobile_number= mobile_num, email = email_,   grade_value=grade_values, review = reviews_)
        adm.save()
        print("data is save")
    return redirect(index)

def admin_office_login(request):
    if request.method == "POST":
        loginusername = request.POST['username_office']
        loginpassword = request.POST['password_office']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            return render(request, "index.html")
        else:
            return redirect(admin_office)

       
        
    

    else:
        return HttpResponse('404 not allowed ')
        
