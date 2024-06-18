import requests
from pprint import pprint

api_key = "c7d3a2711c1ead05d142ce9006c8770a"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "London"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)

if response.status_code == 200:
    data = response.json()
    pprint(data)


    cur_weather = data['main']['temp']

    pressure = data['main']['pressure']
    wind = data['wind']['speed']

    pprint(f"Погода в городе: {city_name}\nТемпература: {cur_weather}C\n"
          f"Давление: {pressure}мм.рт.ст \nВетер: {wind}\n"
          f"Хорошего дня"
else:
    print("Failed to get weather information")