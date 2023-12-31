from django.shortcuts import render
from .api.weather_api import WeatherInfo, CityImage
from django.conf import settings

def weather(request):
    if request.method == "POST":
        city = request.POST.get("city")
        weather_response = WeatherInfo(settings.WEATHER_API_KEY, city)
        image_response = CityImage(settings.UNSPLASH_CLIENT_ID, city)
        print(image_response.json())
        variables = {} 
        variables["weather_info"] = weather_response.json() if weather_response.status_code == 200 else {"error": "City not found"}
        if image_response.status_code == 200 and len(image_response.json().get("results", [])) > 0:
            images = image_response.json()["results"]
            variables["city_images"] = image_response.json()["results"] 
        else:
            variables["city_images"] = {"error": "City not found"}
        
        return render(request, "main/weather.html", variables)
    else:
        return render(request, "main/weather.html", {"weather_info": None, "city_images": None})
