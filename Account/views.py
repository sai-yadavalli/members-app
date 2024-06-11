from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('homepage')
            else:
                return render(request, 'login.html')

    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_obj = User.objects.create_user(username=username, first_name=first_name, last_name=last_name)
        user_obj.set_password(password)
        user_obj.save()
        return redirect('login')
    return render(request, 'register.html')


def logout_view(request):
    user = request.user
    logout(request)
    return redirect('login')
