from django.contrib import messages
from django.contrib.auth import authenticate, login as login_user_in_django, logout as finish_user_session
from django.shortcuts import render, redirect


def login(request):

    if request.method == 'POST':
        username = request.POST.get('form_username')
        password = request.POST.get('form_password')
        user = authenticate(request, usename=username, password= password)
        if user is None:
            messages.error(request, 'Wrong username or password')
        else:
            login_user_in_django(request, user)
            return redirect('home')
    return render(request, 'users/login.html')


def logout(request):
    finish_user_session(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('login')
