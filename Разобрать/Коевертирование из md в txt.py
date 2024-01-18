import os
import pypandoc

# функция для конвертации md в txt
def convert_md_to_txt(md_path, txt_path):
    output = pypandoc.convert_file(md_path, 'plain', outputfile=txt_path)
    return output

# функция для рекурсивного поиска файлов
def search_files(start_dir):
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file == "README.md":
                md_path = os.path.join(root, file)
                txt_path = os.path.join(root, "README.txt")
                convert_md_to_txt(md_path, txt_path)

# вызываем функцию с указанием стартовой директории
start_dir = r'F:\Python PROGRAMS\untitled\Alarm Clock-Будильник'
search_files(start_dir)