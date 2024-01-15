from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

    # You will use 'HttpResponse' if you want to server a simple string.
    # return HttpResponse("Home Page")

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message, date = datetime.today())
        contact.save()
        messages.success(request, "Thanks for being with us. We'll respond you soon!")
    return render(request, "contact.html") 

def services(request):
    return render(request, "services.html")

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")

# Create your views here.
