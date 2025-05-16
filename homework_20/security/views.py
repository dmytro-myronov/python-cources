from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, "customer/register.html", {"form": form})

def login_view(request):
    raise Exception("Not implemented")
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = UserLoginForm()
    return render(request, "customer/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def profile_view(request):
    user = request.user
    if user.is_authenticated:
        return render(request, "customer/profile.html", {"user": user})
    else:
        return redirect('login')

