from django.shortcuts import render
import requests


def index(request):
    appid = 'e8edd503f33a4623b2e6d34e9a1e5c32'
    city = 'Gomel'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=' + appid
    res = requests.get(url).json()
    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon']
    }

    content = {'info': city_info}

    return render(request, 'weather/index.html', content)
