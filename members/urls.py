from django.contrib import admin
from django.urls import path
from . import views as members_views

urlpatterns = [
    path('all_student', members_views.homepage, name='homepage'),
]
