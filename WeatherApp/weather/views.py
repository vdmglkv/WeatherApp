from django.shortcuts import render
from .models import City
from .forms import CityForm
import requests


def index(request):
    appid = 'e8edd503f33a4623b2e6d34e9a1e5c32'
    cities = City.objects.all()

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    all_cities = []
    for city in cities:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city.name}&units=metric&appid=' + appid
        res = requests.get(url).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }
        all_cities.append(city_info)

    content = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', content)


def main(request):
    pass


def about(request):
    pass


def support(request):
    pass

