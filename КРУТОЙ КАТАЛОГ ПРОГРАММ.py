import os
import re
import tkinter as tk
from tkinter import filedialog
from typing import List

def search_programs():
    """Ищет программы в выбранном каталоге, содержащие заданный текст в названии файла или в содержимом."""
    search_term = search_entry.get()
    search_path = search_path_entry.get() or r"F:\Python PROGRAMS\untitled"
    programs: List[str] = []
    if search_path:
        for entry in os.scandir(search_path):
            if entry.is_file() and entry.name.endswith(".py"):
                try:
                    with open(entry.path, "r", encoding="utf-8") as f:
                        program_code = f.read()
                        if search_term and (re.search(r'\b{}\b'.format(re.escape(search_term)), program_code, flags=re.IGNORECASE)
                                            or re.search(r'\b{}\b'.format(re.escape(search_term)), entry.name, flags=re.IGNORECASE)):
                            programs.append(entry.path)
                except OSError:
                    pass
        output_text_widget.delete(1.0, tk.END)
        if programs:
            output_text_widget.insert(tk.END, f"Найдены программы ({len(programs)}):\n")
            for program in programs:
                try:
                    with open(program, "r", encoding="utf-8") as f:
                        program_code = f.read()
                        output_text_widget.insert(tk.END, f"{program}\n{'=' * len(program)}\n")
                        output_text_widget.insert(tk.END, program_code + "\n")
                except OSError:
                    pass
        else:
            output_text_widget.insert(tk.END, "Программы с заданным текстом не найдены.")

def clear_search():
    """Очищает поле поиска и текстовое поле с результатами поиска."""
    search_entry.delete(0, tk.END)
    search_path_entry.delete(0, tk.END)
    search_path_entry.insert(0, r"H:\\Python PROGRAMS\\untitled")
    output_text_widget.delete(1.0, tk.END)

def close_window():
    """Закрывает окно приложения."""
    root.destroy()

root = tk.Tk()
root.geometry("700x500")
root.title("Поиск программ")

# Оформление фрейма поиска
search_frame = tk.Frame(root, pady=10)
search_frame.pack()

search_label = tk.Label(search_frame, text="Текст для поиска:", font=("Arial", 14))
search_label.pack(side=tk.LEFT, padx=10)

search_entry = tk.Entry(search_frame, width=50, font=("Arial", 14))
search_entry.pack(side=tk.LEFT)

# Оформление поля выбора каталога
search_path_frame = tk.Frame(root)
search_path_frame.pack(pady=10)

search_path_label = tk.Label(search_path_frame, text="Каталог для поиска:", font=("Arial", 14))
search_path_label.pack(side=tk.LEFT, padx=10)

search_path_entry = tk.Entry(search_path_frame, width=50, font=("Arial", 14))
search_path_entry.insert(0, r"H:\\Python PROGRAMS\\untitled")
search_path_entry.pack(side=tk.LEFT)

search_path_button = tk.Button(search_path_frame, text="Выбрать", command=lambda: search_path_entry.insert(tk.END, filedialog.askdirectory()), font=("Arial", 14))
search_path_button.pack(side=tk.LEFT, padx=10)

'Оформление кнопок "Поиск" и "Очистить"'
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

search_button = tk.Button(button_frame, text="Поиск", command=search_programs, font=("Arial", 14))
search_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(button_frame, text="Очистить", command=clear_search, font=("Arial", 14))
clear_button.pack(side=tk.LEFT)

'Оформление текстового поля с результатами поиска'
output_text_widget = tk.Text(root, font=("Arial", 14))
output_text_widget.pack(expand=True, fill="both", padx=10, pady=10)

'Оформление кнопки "Закрыть"'
close_button = tk.Button(root, text="Закрыть", command=close_window, font=("Arial", 14))
close_button.pack(side=tk.BOTTOM, pady=10)

root.mainloop()