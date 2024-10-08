import requests

# API key for OpenWeatherMap
API_KEY = "04d438a247212cba6040c7f2c6fcc5bf" #Replace with your actual API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data for {city}")
        return None

def display_weather_data(weather_data):
    if weather_data:
        city = weather_data['name']
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather_description = weather_data['weather'][0]['description']
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {weather_description}")
    else:
        print("No weather data to display")

def main():
    city = input("Enter a city name: ")
    weather_data = get_weather_data(city)
    display_weather_data(weather_data)

if __name__ == "__main__":
    main()
