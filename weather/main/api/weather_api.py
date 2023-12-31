import requests

def WeatherInfo(api_key, city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "units": "metric",
        "q": city,
        "appid": api_key,
    }
    response = requests.get(url, params=params)
    return response

def CityImage(client_id, city):
    headers = {
        "Authorization": f"Client-ID {client_id}"
    }
    url = "https://api.unsplash.com/search/photos/"
    params = {
        "query": city,
        "per_page": 3,
        "orientation": "landscape"
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    return response
