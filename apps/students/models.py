from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone

from apps.corecode.models import StudentClass


class Student(models.Model):
    STATUS_CHOICES = [("active", "Active"), ("inactive", "Inactive")]

    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]

    current_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="active"
    )
    registration_number = models.CharField(max_length=200, unique=True)
    surname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male")
    date_of_birth = models.DateField(default=timezone.now)
    current_class = models.ForeignKey(
        StudentClass, on_delete=models.SET_NULL, blank=True, null=True
    )
    date_of_admission = models.DateField(default=timezone.now)

    mobile_num_regex = RegexValidator(
        regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!"
    )
    parent_mobile_number = models.CharField(
        validators=[mobile_num_regex], max_length=13, blank=True
    )

    address = models.TextField(blank=True)
    others = models.TextField(blank=True)
    passport = models.ImageField(blank=True, upload_to="students/passports/")

    class Meta:
        ordering = ["surname", "firstname", "other_name"]

    def __str__(self):
        return f"{self.surname} {self.firstname} {self.other_name} ({self.registration_number})"

    def get_absolute_url(self):
        return reverse("student-detail", kwargs={"pk": self.pk})


class StudentBulkUpload(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    csv_file = models.FileField(upload_to="students/bulkupload/", blank=True)


class Notice_info(models.Model):
    
    title = models.CharField(max_length = 100,)
    detail = models.TextField(max_length = 1000)
    passport = models.ImageField(blank=True, upload_to="students/notices_file/")
    date = models.DateField(default=timezone.now)


    def __str__(self):
        return self.title

class Vacancy_info(models.Model):
    
    subject = models.CharField(max_length = 100)
    level = models.CharField(max_length = 1000)
    image_vacancy = models.ImageField(blank=True, upload_to="students/vacancy_file/")
    date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=None)

    def __str__(self):
        return self.subject

class Administration_info(models.Model):
    
    name = models.CharField(max_length = 100)
    position = models.CharField(max_length = 1000)
    image_profile = models.ImageField(blank=True, upload_to="students/vacancy_file/")
    description = models.TextField(max_length = 1000)

    def __str__(self):
        return self.position

class Carousel_info(models.Model):
    
    image_name = models.CharField(max_length=20)
    image_carousel = models.ImageField(blank=True, upload_to="students/carousel_file/")

    def __str__(self):
        return self.image_name