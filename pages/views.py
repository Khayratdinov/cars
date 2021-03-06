from django.shortcuts import render
from pages.models import Team
from cars.models import Car
# Create your views here.

def index(request):
    teams = Team.objects.all()

    featured_cars = Car.objects.order_by('-id').filter(is_featured=True)
    all_cars = Car.objects.order_by('-id')
    context = {
        'teams' : teams,
        'featured_cars' : featured_cars,
        'cars' : all_cars
    }
    return render(request, 'pages/home.html', context)


def about(request):
    teams = Team.objects.all()
    context = {
        'teams' : teams
    }
    return render(request, 'pages/about.html', context)


def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')