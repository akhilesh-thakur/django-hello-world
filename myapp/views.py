from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("How are you my friend?")

# Create your views here.
