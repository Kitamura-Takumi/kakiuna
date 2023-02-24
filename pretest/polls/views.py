from django.shortcuts import render, redirect
from .forms import SignupForm,LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup_view(request):
    if request.method == 'POST':

        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = SignupForm()
    
    param = {
        'form': form
    }

    return render(request,'login_app/signup.html', param)

def login_view(request):
    next = request.GET.get('next')
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request, user)
                if next:
                    return redirect(next)
                else:
                    return redirect('')

    else:
        form = LoginForm(request, data=request.POST or None)
        next = request.GET.get('next')

    param = {
        'form': form,
        'next': next
    }

    return render(request, 'login_app/login.html', param)

def logout_view(request):
    logout(request)

    return render(request, 'login_app/logout.html')

@login_required
def user_view(request):
    user = request.user

    params = {
        'user': user
    }

    return render(request, 'login_app/user.html', params)

@login_required
def other_view(request):
    users = User.objects.exclude(username=request.user.username)

    params = {
        'users': users
    }

    return render(request, 'login_app/other.html', params)
