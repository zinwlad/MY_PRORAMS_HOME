# basic_commands.py
from logger_config import logger
from commands import commands
from telebot import types

ALLOWED_USERS = [505934872, 577053144]  # Замените эти числа на реальные ID

def setup_basic_commands(bot, states_menu, csv_filename):
    states = {}
    current_boxes = {}  # Инициализация, если требуется

    def is_user_allowed(message):
        return message.from_user.id in ALLOWED_USERS

    @bot.message_handler(commands=['start'], func=is_user_allowed)
    def handle_start(message):
        logger.info(f"User {message.chat.id} started the conversation.")
        bot.send_message(message.chat.id, "Привет! Этот бот предназначен для управления вашими вещами и коробками.", reply_markup=states_menu)
        states[message.chat.id] = "main_menu"

    @bot.message_handler(func=lambda message: message.text == commands['back'] and is_user_allowed(message))
    def handle_back_button(message):
        logger.info(f"User {message.chat.id} is going back to the main menu.")
        bot.send_message(message.chat.id, "Возвращаемся в главное меню", reply_markup=states_menu)
        states[message.chat.id] = "main_menu"

    return states, current_boxes

# Конец basic_commands.py
