import requests
import os

def get_weather(api_key, city)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get("cod") != 200:
            return f"Error: {data.get('message', 'Unknown error')}"
        weather = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        city_name = data["name"]
        country = data["sys"]["country"]
        return (f"Weather in {city_name}, {country}:\n"
                f"  {weather}\n"
                f"  Temperature: {temp}°C (feels like {feels_like}°C)\n"
                f"  Humidity: {humidity}%")
    except requests.RequestException as e:
        return f"Network error: {e}"

def main():
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("Error: OPENWEATHER_API_KEY environment variable not set.")
        print("Please set your OpenWeatherMap API key in the environment variable and try again.")
        return
    while True:
        city = input("Enter city name (or 'quit' to exit): ").strip()
        if city.lower() == 'quit':
            print("Goodbye!")
            break
        result = get_weather(api_key, city)
        print(result)

if __name__ == "__main__":
    main()
