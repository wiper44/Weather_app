import requests
api_key = '2fb760b470a9c1d72432dd2f880b60fb'
city = 'Kathmandu'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'



response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather_description = data['weather'][0]['description']
    feels_like = data['main']['feels_like']

    print(f"Temperature: {temperature}°C")
    print(f"Temperature Feels Like: {feels_like}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather Description: {weather_description}")