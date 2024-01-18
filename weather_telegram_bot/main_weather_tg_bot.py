import requests
import datetime
import time
import asyncio
import asyncio
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

city_name = None
bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    """
    Обработчик команды /start. Сбрасывает значение переменной city_name.
    """
    global city_name
    city_name = None
    await message.reply("Привет! Напиши город: ")

@dp.message_handler()
async def get_weather(message: types.Message):
    """
    Обработчик сообщения с названием города. Сохраняет название города в переменной city_name и вызывает функцию send_weather().
    """
    global city_name
    if message.text.lower() == "clear":
        city_name = None
        await message.reply("Город сброшен. Пожалуйста, введите новый город.")
    else:
        city_name = message.text
        await send_weather(message)

async def send_weather(message: types.Message):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Pain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U00002600",
        "Show": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        # Получаем данные о погоде из API OpenWeatherMap.
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={open_weather_token}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Извлекаем нужные данные из полученных данных.
        city = data["name"]
        cur_weather = data["main"]["temp"]
        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            weather_emoji = code_to_smile[weather_description]
        else:
            weather_emoji = "Посмотри в окно"

        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = sunset_timestamp - sunrise_timestamp

        await message.reply(f"Погода в городе: {city}\nТемпература: {cur_weather}C° {weather_emoji}\n"
                            f"Влажность: {humidity} %\nДавление: {pressure} мм.рт.ст \nВетер: {wind} м/с\n"
                            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
                            f"Хорошего дня!"
                            )

    except:
        await message.reply('\U00002620 Проверьте название города \U00002620')

async def scheduled_weather(chat_id):
    while True:
        now = datetime.datetime.now()
        if now.hour == 7 and now.minute == 00:
            await bot.send_message(chat_id=chat_id, text="Доброе утро!")

if __name__ == '__main__':
    executor.start_polling(dp)