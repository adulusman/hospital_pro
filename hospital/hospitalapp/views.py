from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import BookingForm


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged successfully')
            return redirect('home')
        else:
            messages.info(request, 'invalid username or password')
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass1']
        cpassword = request.POST['pass2']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                messages.success(request, 'Signup successfully')
                return redirect('login')
        else:
            messages.info(request, 'Password does not match')
            return redirect('register')
    return render(request, 'register.html')


def home(request):
    return render(request, 'home.html')


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    form = BookingForm()
    dict_form = {
        'form': form,
    }
    return render(request, 'booking.html', dict_form)


def department(request):
    depart = {
        'dept': Departments.objects.all()
    }
    return render(request, 'department.html', depart)


def doctor(request):
    doc = {
        'doct': Doctors.objects.all()
    }
    return render(request, 'doctor.html', doc)



def logout(request):
    auth.logout(request)
    return redirect('/')
