# shared.py
import csv
import logging
from commands import commands

def get_existing_boxes(csv_filename):
    existing_boxes = {}
    try:
        with open(csv_filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if 'BoxID' in row and 'BoxName' in row:
                    existing_boxes[row['BoxID']] = row['BoxName']
    except FileNotFoundError as e:
        logging.error(f"Файл {csv_filename} не найден: {e}")
    return existing_boxes

def get_box_contents(csv_filename, box_id):
    contents = []
    try:
        with open(csv_filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get('BoxID') == box_id and 'ItemName' in row:
                    contents.append(row['ItemName'])
    except FileNotFoundError as e:
        logging.error(f"Файл {csv_filename} не найден: {e}")
    return contents

def add_item_to_box(csv_filename, box_id, item):
    try:
        with open(csv_filename, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['BoxID', 'BoxName', 'ItemName'])
            writer.writerow({'BoxID': box_id, 'ItemName': item})
    except FileNotFoundError:
        logging.error(f"Файл {csv_filename} не найден.")

def remove_item_from_box(csv_filename, box_id, item):
    try:
        with open(csv_filename, mode='r', newline='') as file:
            rows = list(csv.DictReader(file))
            rows_to_keep = [row for row in rows if not (row['BoxID'] == box_id and row['ItemName'] == item)]

        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['BoxID', 'BoxName', 'ItemName'])
            writer.writeheader()
            writer.writerows(rows_to_keep)
    except FileNotFoundError:
        logging.error(f"Файл {csv_filename} не найден.")

def add_box(csv_filename, box_name):
    try:
        existing_boxes = get_existing_boxes(csv_filename)
        new_box_id = generate_new_box_id(existing_boxes)

        with open(csv_filename, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['BoxID', 'BoxName', 'ItemName'])
            writer.writerow({'BoxID': new_box_id, 'BoxName': box_name, 'ItemName': ''})
    except FileNotFoundError:
        logging.error(f"Файл {csv_filename} не найден.")

def remove_box(csv_filename, box_id):
    try:
        with open(csv_filename, mode='r', newline='') as file:
            rows = list(csv.DictReader(file))
            rows_to_keep = [row for row in rows if row['BoxID'] != box_id]

        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['BoxID', 'BoxName', 'ItemName'])
            writer.writeheader()
            writer.writerows(rows_to_keep)
    except FileNotFoundError:
        logging.error(f"Файл {csv_filename} не найден.")

def generate_new_box_id(existing_boxes):
    if existing_boxes:
        last_id = max(int(box_id) for box_id in existing_boxes.keys())
        return f"{last_id + 1:06d}"
    else:
        return "000001"

# Конец shared.py