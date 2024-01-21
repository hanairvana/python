# Welcome to my project! 

# Here, I will be using the Openweather API to recieve weather information for the user using openweathermap

import os
import requests

my_secret = "Your Key Here."
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input(str("Enter a city: "))

request_url = f"{BASE_URL}?appid={my_secret}&q={city}&units=imperial"
# print(request_url)
response = requests.get(request_url)

if response.status_code == 200:
  data = response.json()
  weather = data['weather'][0]['description']
  temperaure = data['main']['temp']
  # print(data)
  print("Weather: ",weather)
  print("Temperature: ",temperaure,"*F")
else:
  print("An error occured")
