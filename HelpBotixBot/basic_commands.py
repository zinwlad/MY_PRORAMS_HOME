# basic_commands.py
import logging
from commands import commands
from telebot import types

# Настройка логирования
logging.basicConfig(level=logging.INFO)

def setup_basic_commands(bot, states_menu, csv_filename):
    states = {}
    current_boxes = {}  # Инициализация, если требуется

    @bot.message_handler(commands=['start'])
    def handle_start(message):
        logging.info(f"User {message.chat.id} started the conversation.")
        bot.send_message(message.chat.id, "Привет! Этот бот предназначен для управления вашими вещами и коробками.", reply_markup=states_menu)
        states[message.chat.id] = "main_menu"

    @bot.message_handler(func=lambda message: message.text == "Назад")
    def handle_back_button(message):
        logging.info(f"User {message.chat.id} is going back to the main menu.")
        bot.send_message(message.chat.id, "Возвращаемся в главное меню", reply_markup=states_menu)
        states[message.chat.id] = "main_menu"

    return states, current_boxes

# Конец basic_commands.py
