from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

    # You will use 'HttpResponse' if you want to server a simple string.
    # return HttpResponse("Home Page")

def about(request):
    return HttpResponse("This is About Page")

def contact(request):
    return HttpResponse("Contact Page")

def services(request):
    return HttpResponse("Our Services Page")

# Create your views here.
