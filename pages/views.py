from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')