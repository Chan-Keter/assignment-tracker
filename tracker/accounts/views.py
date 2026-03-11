from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


def register_view(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')

    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'accounts/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def forgot_password(request):
    return render(request,'accounts/forgot-password.html')



def register_view(request):

    if request.method == "POST":

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:

            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

            user.save()

            return redirect('login')

    return render(request, 'accounts/register.html')