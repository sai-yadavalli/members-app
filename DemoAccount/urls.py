from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login_user'),
    path('register', views.register_view, name='register_user'),
    path('logout', views.logout_view, name='logout_user')
]
