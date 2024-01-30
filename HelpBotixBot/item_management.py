# item_management.py

from telebot import types
from shared import get_box_contents, add_item_to_box, remove_item_from_box, get_existing_boxes
from commands import commands

def setup_item_management(bot, csv_filename, items_menu, back_to_main_menu, states, current_boxes):
    # Словарь для хранения введенных вещей перед выбором коробки
    pending_items = {}

    # Обработчик команды "Добавить"
    @bot.message_handler(func=lambda message: message.text == commands['add'])
    def handle_add_item(message):
        bot.send_message(message.chat.id, "Введите название вещи для добавления:", reply_markup=types.ReplyKeyboardRemove())
        states[message.chat.id] = "item_add_name"

    # Обработчик ввода имени вещи
    @bot.message_handler(func=lambda message: states.get(message.chat.id) == "item_add_name")
    def add_item_name(message):
        pending_items[message.chat.id] = message.text
        existing_boxes = get_existing_boxes(csv_filename)
        if not existing_boxes:
            bot.send_message(message.chat.id, "Нет доступных коробок. Сначала создайте коробку.", reply_markup=items_menu)
            states[message.chat.id] = "items_options"
            return

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for box in existing_boxes:
            markup.add(box)
        bot.send_message(message.chat.id, "Выберите коробку для добавления вещи:", reply_markup=markup)
        states[message.chat.id] = "item_add_box"

    # Обработчик выбора коробки для добавления вещи
    @bot.message_handler(func=lambda message: states.get(message.chat.id) == "item_add_box")
    def add_item_to_box_handler(message):
        box_name = message.text
        item_name = pending_items.pop(message.chat.id, None)
        if box_name in get_existing_boxes(csv_filename) and item_name:
            add_item_to_box(csv_filename, box_name, item_name)
            bot.send_message(message.chat.id, f"Вещь '{item_name}' добавлена в коробку '{box_name}'.", reply_markup=items_menu)
        else:
            bot.send_message(message.chat.id, "Ошибка при добавлении вещи. Пожалуйста, попробуйте снова.", reply_markup=items_menu)
        states[message.chat.id] = "items_options"

    # Обработчик команды "Удалить"
    @bot.message_handler(func=lambda message: message.text == commands['delete'])
    def handle_delete_item_init(message):
        existing_boxes = get_existing_boxes(csv_filename)
        if not existing_boxes:
            bot.send_message(message.chat.id, "Нет доступных коробок.", reply_markup=items_menu)
            states[message.chat.id] = "items_options"
            return

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for box in existing_boxes:
            markup.add(box)
        bot.send_message(message.chat.id, "Выберите коробку, из которой хотите удалить вещь:", reply_markup=markup)
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
            bot.send_message(message.chat.id, "Выберите вещь для удаления:", reply_markup=markup)
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