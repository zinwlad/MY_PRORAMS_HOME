# HelpBotixBot_tg.py

import telebot
import os
from telebot import types
from config import bot_token
import basic_commands
import box_management
import item_management
import search_commands
from commands import commands
from barcode_scanner import scan_barcode

csv_filename = os.path.join("my_base", "data.csv")
bot = telebot.TeleBot(bot_token)

# Клавиатуры
states_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
states_menu.row(commands['items'], commands['search'], commands['boxes'], commands['scan'])

items_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
items_menu.row(commands['add'], commands['edit'], commands['delete'])
items_menu.row(commands['back'])

boxes_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
boxes_menu.row(commands['view'], commands['add_box'], commands['delete_box'])
boxes_menu.row(commands['back'])

back_to_main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_to_main_menu.row(commands['back'])

# Инициализация обработчиков команд
states, current_boxes = basic_commands.setup_basic_commands(bot, states_menu, csv_filename)
states, current_boxes = box_management.setup_box_management(bot, csv_filename, states_menu, boxes_menu, back_to_main_menu, states, current_boxes)
states, current_boxes = item_management.setup_item_management(bot, csv_filename, items_menu, back_to_main_menu, states, current_boxes)
states = search_commands.setup_search_commands(bot, csv_filename, states_menu, back_to_main_menu)

# Обработчики команд для новых клавиатур
@bot.message_handler(func=lambda message: message.text == commands['items'])
def handle_items_command(message):
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=items_menu)

def handle_view_boxes_command(message):
    # Получаем словарь существующих коробок
    existing_boxes = get_existing_boxes(csv_filename)  # Словарь {BoxID: BoxName}
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for box_id, box_name in existing_boxes.items():
        markup.add(types.KeyboardButton(box_name))  # Добавляем кнопку с именем коробки, а не ID
    bot.send_message(message.chat.id, "Выберите коробку для просмотра содержимого:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == commands['scan'])
def handle_scan_command(message):
    bot.send_message(message.chat.id, "Отправьте фото штрих-кода.")
    bot.register_next_step_handler(message, process_scan_command)

def process_scan_command(message):
    if message.content_type == 'photo':
        scan_barcode(bot, message, csv_filename)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, отправьте фото штрих-кода.")


# Запуск бота
bot.polling(none_stop=True)

# Конец HelpBotixBot_tg.py