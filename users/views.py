from django.contrib import messages
from django.contrib.auth import authenticate, login as login_user_in_django, logout as finish_user_session
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from users.forms import SignUpForm


class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        username = request.POST.get('form_username')
        password = request.POST.get('form_password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Wrong username or password')
        else:
            login_user_in_django(request, user)
            welcome_url = request.GET.get('next', 'home')
            return redirect(welcome_url)
        return render(request, 'users/login.html')


class LogoutView(View):
    def get(self, request):
        finish_user_session(request)
        messages.success(request, 'You have been logged out successfully!')
        return redirect('login')


class SignUpView(View):

    def get(self, request):
        form = SignUpForm()
        return render(request, 'users/signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = User()
            new_user.username = form.cleaned_data.get('username')
            new_user.first_name = form.cleaned_data.get('first_name')
            new_user.last_name = form.cleaned_data.get('last_name')
            new_user.email = form.cleaned_data.get('email')
            new_user.set_password(form.cleaned_data.get('password'))
            new_user.save()
            messages.success(request, 'User registered successfully!')
            form = SignUpForm()
            if messages.success:
                return redirect('home')
        return render(request, 'users/signup.html', {'form': form})


class UsersBlogsListView(ListView):
    model = User
    template_name = 'users/blogs_list.html'

