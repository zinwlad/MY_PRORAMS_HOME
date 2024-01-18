# box_management.py

from telebot import types
from shared import get_existing_boxes, get_box_contents, add_box, remove_box


def setup_box_management(bot, csv_filename, states_menu, boxes_menu, back_to_main_menu, states, current_boxes):
    # Обработчик команды "Коробки"
    @bot.message_handler(func=lambda message: message.text == "Коробки")
    def handle_boxes_command(message):
        bot.send_message(message.chat.id, "Выберите действие:", reply_markup=boxes_menu)
        states[message.chat.id] = "boxes_options"

    # Обработчик команды "Просмотр"
    @bot.message_handler(func=lambda message: message.text == "Просмотр" and states.get(message.chat.id) == "boxes_options")
    def handle_view_boxes_command(message):
        existing_boxes = get_existing_boxes(csv_filename)
        if not existing_boxes:
            bot.send_message(message.chat.id, "Нет доступных коробок для просмотра.", reply_markup=boxes_menu)
            return
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for box_name in existing_boxes:
            markup.add(box_name)
        bot.send_message(message.chat.id, "Выберите коробку для просмотра содержимого:", reply_markup=markup)
        states[message.chat.id] = "box_view_choice"

    # Обработчик выбора коробки для просмотра
    @bot.message_handler(func=lambda message: states.get(message.chat.id) == "box_view_choice")
    def handle_box_view_choice(message):
        selected_box = message.text
        contents = get_box_contents(csv_filename, selected_box)
        if contents:
            reply_message = f"Содержимое коробки '{selected_box}':\n" + "\n".join(contents)
        else:
            reply_message = f"Коробка '{selected_box}' пуста."
        bot.send_message(message.chat.id, reply_message, reply_markup=back_to_main_menu)
        states[message.chat.id] = "main_menu"

    # Обработчик команды "Добавить коробку"
    @bot.message_handler(func=lambda message: message.text == "Добавить коробку" and states.get(message.chat.id) == "boxes_options")
    def handle_add_box_command(message):
        bot.send_message(message.chat.id, "Введите название новой коробки:", reply_markup=types.ReplyKeyboardRemove())
        states[message.chat.id] = "add_box"

    # Обработчик для ввода названия новой коробки
    @bot.message_handler(func=lambda message: states.get(message.chat.id) == "add_box")
    def add_box_handler(message):
        box_name = message.text
        add_box(csv_filename, box_name)  # Ваша функция для добавления коробки
        bot.send_message(message.chat.id, f"Коробка '{box_name}' добавлена.", reply_markup=boxes_menu)
        states[message.chat.id] = "boxes_options"

    # Обработчик команды "Удалить коробку"
    @bot.message_handler(func=lambda message: message.text == "Удалить коробку" and states.get(message.chat.id) == "boxes_options")
    def handle_delete_box_command(message):
        existing_boxes = get_existing_boxes(csv_filename)
        if not existing_boxes:
            bot.send_message(message.chat.id, "Нет доступных коробок для удаления.", reply_markup=boxes_menu)
            return
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for box_name in existing_boxes:
            markup.add(box_name)
        bot.send_message(message.chat.id, "Выберите коробку для удаления:", reply_markup=markup)
        states[message.chat.id] = "delete_box"

    # Обработчик выбора коробки для удаления
    @bot.message_handler(func=lambda message: states.get(message.chat.id) == "delete_box")
    def delete_box_handler(message):
        box_name = message.text
        remove_box(csv_filename, box_name)  # Ваша функция для удаления коробки
        bot.send_message(message.chat.id, f"Коробка '{box_name}' удалена.", reply_markup=boxes_menu)
        states[message.chat.id] = "boxes_options"
    # Обработчик команды "Назад"
    @bot.message_handler(func=lambda message: message.text == "Назад" and states.get(message.chat.id) == "boxes_options")
    def handle_back_button_in_boxes(message):
        bot.send_message(message.chat.id, "Возвращаемся в главное меню", reply_markup=states_menu)
        states[message.chat.id] = "main_menu"

    return states, current_boxes
