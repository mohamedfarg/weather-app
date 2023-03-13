from django.shortcuts import render
import requests
from django.http import JsonResponse
# Create your views here.
def index(request):
    
    api_key = "87fb5052a93048f3be5103659231303"
    city = "cairo"  # Replace with the name of the city you want weather data for

    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    print(url)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp_c = data['current']['temp_c'] # get current temperature in celsius
        condition = data['current']['condition']['text'] # get current condition
        wind_speed = data['current']['wind_kph'] # get current wind speed in kph
        humidity = data['current']['humidity'] # get current humidity

        context = {
            'city':city,
            'temp_c': temp_c,
            'condition': condition,
            'wind_speed': wind_speed,
            'humidity': humidity
        }

        return render(request, "index.html",context)
    else:
        return render(request, "404.html")