# search_commands.py
from logger_config import logger
from telebot import types
import csv
from commands import commands

# Функции для работы с CSV...
def get_existing_boxes(csv_filename):
    boxes = set()
    with open(csv_filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            boxes.add(row['BoxName'])
    return boxes

# Предполагаемая структура функции get_box_contents
def get_box_contents(csv_filename, box_name):
    items = []
    with open(csv_filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['BoxName'] == box_name:
                items.append(row['ItemName'])
    return items

def setup_search_commands(bot, csv_filename, states_menu, back_to_main_menu):
    states = {}  # Словарь для хранения состояний пользователей

    @bot.message_handler(func=lambda message: message.text == commands['search'])
    def handle_search_command(message):
        logger.info(f"Пользователь {message.chat.id} начал поиск вещи.")
        bot.send_message(message.chat.id, "Введите название вещи для поиска:", reply_markup=types.ReplyKeyboardRemove())
        states[message.chat.id] = "item_search"

    @bot.message_handler(func=lambda message: states.get(message.chat.id) == "item_search")
    def search_item(message):
        item_name = message.text
        logger.info(f"Пользователь {message.chat.id} ищет вещь '{item_name}'.")

        found = False
        for box_name in get_existing_boxes(csv_filename):
            if item_name in get_box_contents(csv_filename, box_name):
                bot.send_message(message.chat.id, f"Вещь '{item_name}' найдена в коробке '{box_name}'.",
                                 reply_markup=states_menu)
                logger.info(f"Вещь '{item_name}' найдена в коробке '{box_name}' для пользователя {message.chat.id}.")
                found = True
                break

        if not found:
            bot.send_message(message.chat.id,
                             f"Вещь '{item_name}' не найдена. Попробуйте еще раз или вернитесь в главное меню.",
                             reply_markup=back_to_main_menu)
            logger.info(f"Вещь '{item_name}' не найдена для пользователя {message.chat.id}.")

        states[message.chat.id] = "main_menu"

    @bot.message_handler(func=lambda message: message.text == "Назад")
    def handle_back_button(message):
        bot.send_message(message.chat.id, "Возвращаемся в главное меню", reply_markup=states_menu)
        states[message.chat.id] = "main_menu"

    return states

# Конец search_commands.py