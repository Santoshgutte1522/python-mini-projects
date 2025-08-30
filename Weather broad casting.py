import requests

# Replace with your real API key

API_KEY = "480180f18a4bd477133e6e1821d05529"
CITY = input("Enter City: ")
URL =f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Send GET request

response = requests.get(URL)

# Check if request was successful

if response.status_code == 200:
 data = response.json()

 # Extract weather info
 print(data)
 city = data['name']
 temp = data['main']['temp']
 weather = data['weather'][0]['description']
 humidity = data['main']['humidity']
 wind_speed = data['wind']['speed']
 print(f" City: {city}")
 print(f"🌡 Temperature: {temp}°C")
 print(f" Weather: {weather}")
 print(f" Humidity: {humidity}%")
 print(f" Wind Speed: {wind_speed} m/s")
else:
 print(" Failed to retrieve weather data. Check your API key or city name.")