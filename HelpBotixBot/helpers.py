# helpers.py
from logger_config import logger

def is_text_message(message):
    logger.debug(f"Проверка типа сообщения: {message.content_type}")
    return message.content_type == 'text'

def clean_and_lower(text):
    logger.info(f"Очистка и приведение текста к нижнему регистру: {text}")
    cleaned_text = text.strip().lower()
    return cleaned_text

# Конец helpers.py
