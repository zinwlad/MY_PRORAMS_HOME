# item_management.py

from telebot import types
from shared import get_box_contents, add_item_to_box, remove_item_from_box, get_existing_boxes
from commands import commands
import logging

# Настройка логирования с обработчиком файла
logging.basicConfig(filename='item_management.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def setup_item_management(bot, csv_filename, items_menu, back_to_main_menu, states, current_boxes):
    # Словарь для хранения введенных вещей перед выбором коробки
    pending_items = {}

    # Обработчик команды "Добавить"
    @bot.message_handler(func=lambda message: message.text == commands['add'])
    def handle_add_item(message):
        bot.send_message(message.chat.id, "Введите название вещи:")
        states[message.chat.id] = "item_add_name"

    # Обработчик ввода имени вещи
    @bot.message_handler(func=lambda message: states.get(message.chat.id) == "item_add_name")
    def add_item_name(message):
        pending_items[message.chat.id] = message.text
        boxes = get_existing_boxes(csv_filename)  # Словарь {BoxID: BoxName}
        if not boxes:
            bot.send_message(message.chat.id, "Нет коробок. Сначала создайте коробку.", reply_markup=items_menu)
            states[message.chat.id] = "items_options"
            return
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for box_name in boxes.values():
            markup.add(types.KeyboardButton(box_name))
        bot.send_message(message.chat.id, "Выберите коробку:", reply_markup=markup)
        states[message.chat.id] = "item_add_box"

    # Обработчик выбора коробки для добавления вещи
    @bot.message_handler(func=lambda message: states.get(message.chat.id) == "item_add_box")
    def add_item_to_box_handler(message):
        box_name = message.text
        box_id = None
        existing_boxes = get_existing_boxes(csv_filename)
        for key, value in existing_boxes.items():
            if value == box_name:
                box_id = key
                break

        item_name = pending_items.pop(message.chat.id, None)
        if box_id and item_name:
            add_item_to_box(csv_filename, box_id, item_name, bot, message, items_menu)
            bot.send_message(message.chat.id, f"Вещь '{item_name}' добавлена в коробку '{box_name}'.",
                             reply_markup=items_menu)
        else:
            bot.send_message(message.chat.id, "Ошибка. Не удалось найти коробку. Попробуйте снова.",
                             reply_markup=items_menu)
        states[message.chat.id] = "items_options"

    # Обработчик команды "Удалить"
    @bot.message_handler(func=lambda message: message.text == commands['delete'])
    def handle_delete_item_init(message):
        boxes = get_existing_boxes(csv_filename)
        if not boxes:
            bot.send_message(message.chat.id, "Нет коробок.", reply_markup=items_menu)
            states[message.chat.id] = "items_options"
            return
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for box in boxes:
            markup.add(box)
        bot.send_message(message.chat.id, "Выберите коробку:", reply_markup=markup)
        states[message.chat.id] = "item_delete_box"

    # Обработчик выбора коробки для удаления вещи
    @bot.message_handler(func=lambda message: states.get(message.chat.id) == "item_delete_box")
    def handle_box_choice_for_delete(message):
        selected_box = message.text
        current_boxes[message.chat.id] = selected_box
        contents = get_box_contents(csv_filename, selected_box)
        if contents:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for item in contents:
                markup.add(item)
            bot.send_message(message.chat.id, "Выберите вещь:", reply_markup=markup)
            states[message.chat.id] = "item_delete"
        else:
            bot.send_message(message.chat.id, "Коробка пуста.", reply_markup=items_menu)
            states[message.chat.id] = "items_options"

    # Обработчик для удаления вещи
    @bot.message_handler(func=lambda message: states.get(message.chat.id) == "item_delete")
    def delete_item(message):
        box_name = current_boxes[message.chat.id]
        item_to_delete = message.text
        if item_to_delete in get_box_contents(csv_filename, box_name):
            remove_item_from_box(csv_filename, box_name, item_to_delete)
            bot.send_message(message.chat.id, f"Вещь '{item_to_delete}' удалена из коробки '{box_name}'.",
                             reply_markup=items_menu)
        else:
            bot.send_message(message.chat.id, "Ошибка: вещь не найдена.", reply_markup=items_menu)
        states[message.chat.id] = "items_options"

    # Возвращаем измененные states и current_boxes
    return states, current_boxes

# Конец item_management.py