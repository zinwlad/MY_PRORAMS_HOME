from translate import Translator
import os

# Указываем путь к папке, которую нужно перевести
folder_path = "F:\\Python PROGRAMS\\untitled\\python-beginner-projects\\projects"

# Создаем экземпляр класса Translator
translator = Translator(to_lang='ru')

# Получаем список папок в указанной директории
folders = os.listdir(folder_path)

# Переводим названия папок с английского на русский язык
for folder in folders:
    translated_text = translator.translate(folder)
    new_folder_name = f"{folder}-{translated_text}".replace(':', '')
    new_folder_path = os.path.join(folder_path, new_folder_name)
    if os.path.exists(new_folder_path):
        print(f"Папка {new_folder_name} уже существует!")
        continue
    os.rename(
        os.path.join(folder_path, folder),
        new_folder_path
    )
    print(f"Переведено: {folder} -> {new_folder_name}")