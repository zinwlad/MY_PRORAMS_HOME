# shared.py
import csv
import logging

def get_existing_boxes(csv_filename):
    existing_boxes = set()
    try:
        with open(csv_filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if 'BoxName' in row:  # Проверяем, есть ли ключ 'BoxName' в строке
                    existing_boxes.add(row['BoxName'])
                else:
                    logging.warning("В строке CSV отсутствует ключ 'BoxName'.")
    except FileNotFoundError as e:
        logging.error(f"Файл {csv_filename} не найден: {e}")
    return list(existing_boxes)

def get_box_contents(csv_filename, box_name):
    contents = []
    try:
        with open(csv_filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if 'BoxName' in row and row['BoxName'] == box_name:
                    if 'ItemName' in row:  # Изменено здесь
                        contents.append(row['ItemName'])  # Изменено здесь
                    else:
                        logging.warning("В строке CSV отсутствует ключ 'ItemName'.")  # Изменено здесь
    except FileNotFoundError as e:
        logging.error(f"Файл {csv_filename} не найден: {e}")
    except KeyError as e:
        logging.error(f"Столбец 'ItemName' не найден в файле {csv_filename}: {e}")  # Изменено здесь
    return contents

def add_item_to_box(csv_filename, box_name, item):
    try:
        with open(csv_filename, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['BoxName', 'ItemName'])
            writer.writerow({'BoxName': box_name, 'ItemName': item})
    except FileNotFoundError:
        print(f"Файл {csv_filename} не найден.")

def remove_item_from_box(csv_filename, box_name, item):
    try:
        with open(csv_filename, mode='r', newline='') as file:
            rows = list(csv.DictReader(file))
            rows_to_keep = [row for row in rows if not (row['BoxName'] == box_name and row['ItemName'] == item)]

        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['BoxName', 'ItemName'])
            writer.writeheader()
            writer.writerows(rows_to_keep)
    except FileNotFoundError:
        print(f"Файл {csv_filename} не найден.")

def add_box(csv_filename, box_name):
    """Добавляет новую коробку в CSV-файл."""
    try:
        with open(csv_filename, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['BoxName', 'ItemName'])
            writer.writerow({'BoxName': box_name, 'ItemName': ''})  # Добавляем коробку без вещей
    except FileNotFoundError:
        logging.error(f"Файл {csv_filename} не найден.")

def remove_box(csv_filename, box_name):
    """Удаляет коробку и все ее содержимое из CSV-файла."""
    try:
        with open(csv_filename, mode='r', newline='') as file:
            rows = list(csv.DictReader(file))
            rows_to_keep = [row for row in rows if row['BoxName'] != box_name]

        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['BoxName', 'ItemName'])
            writer.writeheader()
            writer.writerows(rows_to_keep)
    except FileNotFoundError:
        logging.error(f"Файл {csv_filename} не найден.")