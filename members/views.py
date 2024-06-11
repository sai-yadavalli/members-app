from django.shortcuts import render, redirect
from . import models as members_models


# Create your views here.


def homepage(request):
    all_student = members_models.Student.objects.all()  # this technique is called ORM (Object Relational Mapping)
    context = {
        'all_student': all_student,
    }
    return render(request, 'home.html', context)

def disciples_page(request):
    all_student = members_models.Student.objects.all()
    context = {
        'all_student': all_student,
    }
    return render(request, 'disciples.html', context)

def years_page(request):
    all_student = members_models.Student.objects.all()
    context = {
        'all_student': all_student,
    }
    return render(request, 'years.html', context)