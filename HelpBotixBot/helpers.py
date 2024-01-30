# helpers.py
import logging

logging.basicConfig(
    filename='helpers.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

def is_text_message(message):
    logging.debug(f"Проверка типа сообщения: {message.content_type}")
    return message.content_type == 'text'

def clean_and_lower(text):
    logging.info(f"Очистка и приведение текста к нижнему регистру: {text}")
    cleaned_text = text.strip().lower()
    return cleaned_text

# Конец helpers.py
