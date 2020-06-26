from django.shortcuts import render

import requests
from .models import city 
from .forms import city_form


# Create your views here.
def home(request):


    url='http://api.openweathermap.org/data/2.5/weather?q=India&units=imperial&appid=f6a2db50ce45d87de65cf404b5b8983e'
    cities=city.objects.all()
    if request.method == 'POST':
        form = city_form(request.POST)
        form.save()

    form=city_form
    weather_data=[]
    
    for City in cities:

        # request the json data and convert it into Python data_types
        city_weather=requests.get(url.format(city)).json()

        # Dictionary for getting api objects
        weather = {
            'city' : City.name,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        
        weather_data.append(weather)

    context = {'weather_data' : weather_data  ,  'form': form }
    return render(request,'home.html' , context)



