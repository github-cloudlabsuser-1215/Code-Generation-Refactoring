import requests

#Fetch weather data from openweathermap.org
def fetch_weather_data(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code

# Example usage
api_key = "3b05595ab8b60248be793bbbe3bb6243"
city = "London"
weather_data = fetch_weather_data(api_key, city)
if weather_data:
    print(weather_data)
else:
    print("Failed to fetch weather data")