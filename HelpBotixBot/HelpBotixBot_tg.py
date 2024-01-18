# HelpBotixBot_tg.py

import telebot
import os
from telebot import types
from config import bot_token
import basic_commands
import box_management
import item_management
import search_commands

# Задаем путь к файлу CSV
csv_filename = os.path.join("my_base", "data.csv")

# Инициализация бота с токеном из файла конфигурации
bot = telebot.TeleBot(bot_token)

# Клавиатуры
states_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
states_menu.row("Вещи", "Поиск", "Коробки")

items_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
items_menu.row("Добавить", "Редактировать", "Удалить")
items_menu.row("Назад")

boxes_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
boxes_menu.row("Просмотр", "Добавить коробку", "Удалить коробку")
boxes_menu.row("Назад")

back_to_main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_to_main_menu.row("Назад")

# Инициализация обработчиков команд
states, current_boxes = basic_commands.setup_basic_commands(bot, states_menu, csv_filename)
states, current_boxes = box_management.setup_box_management(bot, csv_filename, states_menu, boxes_menu, back_to_main_menu, states, current_boxes)
states, current_boxes = item_management.setup_item_management(bot, csv_filename, items_menu, back_to_main_menu, states, current_boxes)
states = search_commands.setup_search_commands(bot, csv_filename, states_menu, back_to_main_menu)  # Добавлен back_to_main_menu

# Обработчики команд для новых клавиатур
@bot.message_handler(func=lambda message: message.text == "Вещи")
def handle_items_command(message):
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=items_menu)

@bot.message_handler(func=lambda message: message.text == "Коробки")
def handle_boxes_command(message):
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=boxes_menu)

# Запуск бота
bot.polling(none_stop=True)
