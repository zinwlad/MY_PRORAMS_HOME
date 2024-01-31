# item_management.py
from logger_config import logger
from telebot import types
from shared import remove_item_from_box, get_existing_boxes, get_box_contents, add_box, add_item_to_box
from commands import commands

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
        box_id_input = message.text
        existing_boxes = get_existing_boxes(csv_filename)

        if box_id_input in existing_boxes:
            box_name = existing_boxes[box_id_input]
            current_boxes[message.chat.id] = (box_id_input, box_name)
            contents = get_box_contents(csv_filename, box_id_input)
            if contents:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                for item in contents:
                    markup.add(item)
                bot.send_message(message.chat.id, "Выберите вещь:", reply_markup=markup)
                states[message.chat.id] = "item_delete"
            else:
                bot.send_message(message.chat.id, "Коробка пуста.", reply_markup=items_menu)
                states[message.chat.id] = "items_options"
        else:
            bot.send_message(message.chat.id, "Коробка не найдена.", reply_markup=items_menu)
            states[message.chat.id] = "items_options"

    # Обработчик для удаления вещи
    @bot.message_handler(func=lambda message: states.get(message.chat.id) == "item_delete")
    def delete_item(message):
        item_to_delete = message.text
        box_id, box_name = current_boxes[message.chat.id]  # Получаем ID и название коробки
        if item_to_delete in get_box_contents(csv_filename, box_id):
            remove_item_from_box(csv_filename, box_id, item_to_delete)
            bot.send_message(message.chat.id, f"Вещь '{item_to_delete}' удалена из коробки '{box_name}'.",
                             reply_markup=items_menu)
        else:
            bot.send_message(message.chat.id, "Ошибка: вещь не найдена.", reply_markup=items_menu)
        states[message.chat.id] = "items_options"

    # Возвращаем измененные states и current_boxes
    return states, current_boxes

# Конец item_management.py