# helpers.py
def is_text_message(message):
    return message.content_type == 'text'

def clean_and_lower(text):
    cleaned_text = text.strip().lower()
    return cleaned_text

# Конец кода helpers.py