import requests

def get_weather(city):
    api_key = 'YOUR_API_KEY'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    if data['cod'] == 200:
        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        return weather_info
    else:
        return None

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather = get_weather(city)
    if weather:
        print(f"Current weather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description']}")
    else:
        print("City not found.")