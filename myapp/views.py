from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

    # You will use 'HttpResponse' if you want to server a simple string.
    # return HttpResponse("Home Page")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def services(request):
    return render(request, "services.html")

# Create your views here.
