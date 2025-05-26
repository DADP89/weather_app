import requests

def fetch_weather_data(api_key: str, city_name: str):
    base_url = "https://api.weatherapi.com/v1/forecast.json"
    params = {
        "key": api_key,
        "q": city_name,
        "days": 1,
        "aqi": "no",
        "alerts": "no"
    }
    
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return response.json()