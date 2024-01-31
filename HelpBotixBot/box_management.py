# box_management.py
from logger_config import logger
from telebot import types
from shared import get_existing_boxes, get_box_contents, add_box, remove_box
from commands import commands

def setup_box_management(bot, csv_filename, states_menu, boxes_menu, back_to_main_menu, states, current_boxes):
    # Обработчик команды "Коробки"
    @bot.message_handler(func=lambda message: message.text == "Коробки")
    def handle_boxes_command(message):
        logger.info("Обработчик команды 'Коробки' вызван.")
        bot.send_message(message.chat.id, "Выберите действие:", reply_markup=boxes_menu)
        states[message.chat.id] = "boxes_options"

    # Обработчик команды "Просмотр"
    @bot.message_handler(func=lambda message: message.text == commands['view'])
    def handle_view_boxes_command(message):
        existing_boxes = get_existing_boxes(csv_filename)
        if not existing_boxes:
            bot.send_message(message.chat.id, "Нет доступных коробок для просмотра.", reply_markup=boxes_menu)
            return
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # Используйте items(), чтобы получить и BoxID, и BoxName
        for box_id, box_name in existing_boxes.items():
            markup.add(types.KeyboardButton(box_name))  # Добавляем кнопку с названием коробки
        bot.send_message(message.chat.id, "Выберите коробку для просмотра содержимого:", reply_markup=markup)
        states[message.chat.id] = "box_view_choice"

    # Обработчик выбора коробки для просмотра
    @bot.message_handler(func=lambda message: states.get(message.chat.id) == "box_view_choice")
    def handle_box_view_choice(message):
        selected_box_name = message.text
        box_id = None
        # Получаем BoxID, соответствующий выбранному BoxName
        for box_id_iter, box_name_iter in get_existing_boxes(csv_filename).items():
            if box_name_iter == selected_box_name:
                box_id = box_id_iter
                break
        if box_id is None:
            bot.send_message(message.chat.id, f"Коробка с именем '{selected_box_name}' не найдена.",
                             reply_markup=boxes_menu)
            return
        contents = get_box_contents(csv_filename, box_id)
        if contents:
            reply_message = f"Содержимое коробки '{selected_box_name}':\n" + "\n".join(contents)
        else:
            reply_message = f"Коробка '{selected_box_name}' пуста."
        bot.send_message(message.chat.id, reply_message, reply_markup=back_to_main_menu)
        states[message.chat.id] = "main_menu"

    # Обработчик команды "Добавить коробку"
    @bot.message_handler(func=lambda message: message.text == commands['add_box'])
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
    @bot.message_handler(func=lambda message: message.text == commands['delete_box'])
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
        selected_box_name = message.text
        box_id_to_delete = None
        existing_boxes = get_existing_boxes(csv_filename)

        for box_id, box_name in existing_boxes.items():
            if box_name == selected_box_name:
                box_id_to_delete = box_id
                break

        if box_id_to_delete is None:
            bot.send_message(message.chat.id, f"Коробка с именем '{selected_box_name}' не найдена.",
                             reply_markup=boxes_menu)
        else:
            remove_box(csv_filename, box_id_to_delete)  # Используйте BoxID для удаления
            bot.send_message(message.chat.id, f"Коробка '{selected_box_name}' удалена.", reply_markup=boxes_menu)
        states[message.chat.id] = "boxes_options"

    # Обработчик команды "Назад"
    @bot.message_handler(func=lambda message: message.text == "Назад" and states.get(message.chat.id) == "boxes_options")
    def handle_back_button_in_boxes(message):
        bot.send_message(message.chat.id, "Возвращаемся в главное меню", reply_markup=states_menu)
        states[message.chat.id] = "main_menu"

    return states, current_boxes

# Конец box_management.py