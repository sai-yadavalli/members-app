from django.contrib import admin
from django.urls import path
from . import views as account_views

urlpatterns = [
    path('', account_views.login_view, name='login'),
    path('register', account_views.register_view, name='register_sai'),
    path('logout', account_views.logout_view, name='logout'),

]
