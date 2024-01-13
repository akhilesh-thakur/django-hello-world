from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Home Page")

def about(request):
    return HttpResponse("This is About Page")

def contact(request):
    return HttpResponse("Contact Page")

def services(request):
    return HttpResponse("Our Services Page")

# Create your views here.
