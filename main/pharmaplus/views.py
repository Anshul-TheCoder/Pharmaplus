from django.shortcuts import render
from pharmaplus.models import FeedBack
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import City, Medicine, Stores, Availability
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout as _logout
from django.contrib.auth import login as _login
from django.contrib import messages
# Create your views here.


def index(request):


    if request.method == 'POST':
        medicine = request.POST['s_medicine']
        city = request.POST['s_city']

        stores = Stores.objects.filter(availability__medicine__name=medicine).filter(city__city=city).filter(availability__quantity__gt = 0).distinct()

        context = {
            "stores" : stores
        }

        return render(request, 'result.html', context)

        

    cities = City.objects.all()
    medicines = Medicine.objects.all()

    context = {
        "cities" : cities,
        "medicines" : medicines
    }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def thankyou(request):
    return render(request, 'thankyou.html')

def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        try:
            _login(request, user)
        except:
            messages.info(request, "Invalid Credentials")
            return HttpResponseRedirect(reverse("pharmaplus:index"))

        return HttpResponseRedirect(reverse("pharmaplus:index"))


    return render(request, 'login.html')

def logout(request):
    _logout(request)
    return render(request, 'index.html')


def contact(request):

    if request.method == 'POST':
        p = FeedBack()
        p.first_name = request.POST['c_fname']
        p.last_name = request.POST['c_lname']
        p.email = request.POST['c_email']
        p.subject = request.POST['c_subject']
        p.message = request.POST['c_message']
        p.save()
        return HttpResponseRedirect(reverse('pharmaplus:index'))

    return render(request, 'contact.html')

def register(request):

    if request.method == "POST":
        first_name = request.POST['c_fname']
        last_name = request.POST['c_lname']
        username = request.POST['c_uname']
        email = request.POST['c_email']
        password = request.POST['c_pass1']
        rePassword = request.POST['c_pass2']
        type_of_customer = request.POST['type_of_user']


        if password != rePassword:
            messages.info(request, "Password does not match")
            return HttpResponseRedirect(reverse("pharmaplus:index"))

        
        try:
            us = User.objects.create_user(username = username, email=email, password=password)
            us.first_name = first_name
            us.last_name = last_name
            us.save()
            return HttpResponseRedirect(reverse("pharmaplus:index"))
        except:
            messages.info(request, "User creation error")
            return HttpResponseRedirect(reverse("pharmaplus:index"))






    return render(request, 'register.html')