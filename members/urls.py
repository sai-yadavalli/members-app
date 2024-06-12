from django.contrib import admin
from django.urls import path
from . import views as members_views

urlpatterns = [
    path('', members_views.homepage, name='homepage'),
    path('/disciples', members_views.disciples_page, name='disciples'),
    path('/years', members_views.years_page, name='years')
]
