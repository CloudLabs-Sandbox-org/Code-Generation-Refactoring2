import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

# Replace 'your_api_key' with your actual OpenWeatherMap API key
api_key = 'your_api_key'
city = 'Madrid'
weather_data = get_weather(api_key, city)

if weather_data:
    print(f"City: {weather_data['name']}")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Weather: {weather_data['weather'][0]['description']}")
else:
    print("Error fetching weather data")
   