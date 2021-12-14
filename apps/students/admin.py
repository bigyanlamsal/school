from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Student)
admin.site.register(models.StudentBulkUpload)
admin.site.register(models.Notice_info)
admin.site.register(models.Vacancy_info)
admin.site.register(models.Carousel_info)