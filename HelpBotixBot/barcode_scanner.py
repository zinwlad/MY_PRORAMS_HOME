# barcode_scanner.py

import io
from telebot import types
from pyzbar.pyzbar import decode
from PIL import Image
import csv

def scan_barcode(bot, message, csv_filename):
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    image_stream = io.BytesIO(downloaded_file)
    image = Image.open(image_stream)

    decoded_objects = decode(image)
    for obj in decoded_objects:
        box_id = obj.data.decode('utf-8')  # Декодируем данные QR-кода
        contents = check_box_number(box_id, csv_filename)
        bot.reply_to(message, contents)

def check_box_number(box_id, csv_filename):
    box_name = None
    items = []
    with open(csv_filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['BoxID'] == box_id:
                if not box_name:
                    box_name = row['BoxName']  # Запоминаем название коробки
                items.append(row['ItemName'])
        print(f"Проверяемый BoxID: {box_id}")  # Отладочный вывод
        if box_name:
            if items:
                return f"Коробка '{box_name}' ({box_id}) содержит: " + ", ".join(items)
            else:
                return f"Коробка '{box_name}' ({box_id}) пуста."
        else:
            return f"Коробка с номером {box_id} не найдена."


# Конец barcode_scanner.py