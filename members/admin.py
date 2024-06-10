from django.contrib import admin
from .models import Student
from .models import Class
from .models import Disciple

# Register your models here.
admin.site.register(Class)
admin.site.register(Disciple)
admin.site.register(Student)