from django.contrib import admin
from .models import Department,Section,Semester,Student

# Register your models here.
admin.site.register(Department)
admin.site.register(Section)
admin.site.register(Semester)
admin.site.register(Student)
