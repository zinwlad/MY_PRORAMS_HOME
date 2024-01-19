import tkinter as tk
from tkinter import messagebox

def calculate_num_rectangles(rect_length, rect_width, paper_length, paper_width):
    if not 0 < rect_length <= paper_length or not 0 < rect_width <= paper_width:
        raise ValueError("Неверные размеры прямоугольника или бумаги.")
    return (paper_width // rect_width) * (paper_length // rect_length)

def calculate_and_display_results():
    try:
        rect_length = int(length_entry.get())
        rect_width = int(width_entry.get())
        if rect_length <= 0 or rect_width <= 0:
            raise ValueError("Длина и ширина должны быть положительными числами.")
        paper_sizes = [(297, 210), (210, 297), (420, 297), (297, 420), (450, 320), (320, 450)]
        results = [calculate_num_rectangles(rect_length, rect_width, paper_length, paper_width) for paper_length, paper_width in paper_sizes]
        result_texts = ["A4 горизонтально", "A4 вертикально", "A3 горизонтально", "A3 вертикально", "SRA3 горизонтально", "SRA3 вертикально"]
        for label, result in zip(result_labels, results):
            label.config(text=f"Количество прямоугольников на листе {result_texts[result_labels.index(label)]}: {result}")
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))
    except TypeError:
        messagebox.showerror("Ошибка", "Введите корректные числа.")

def clear_entries():
    length_entry.delete(0, tk.END)
    width_entry.delete(0, tk.END)
    for label in result_labels:
        label.config(text="")

root = tk.Tk()
root.title("Расчет количества прямоугольников на листе бумаги")

def create_label_entry_pair(text, row):
    label = tk.Label(root, text=text)
    label.grid(row=row, column=0, padx=5, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=row, column=1, padx=5, pady=5)
    return entry

length_entry = create_label_entry_pair("Длина прямоугольника (мм):", 0)
width_entry = create_label_entry_pair("Ширина прямоугольника (мм):", 1)

calculate_button = tk.Button(root, text="Рассчитать", command=calculate_and_display_results)
calculate_button.grid(row=2, column=0, padx=5, pady=5)

clear_button = tk.Button(root, text="Очистить", command=clear_entries)
clear_button.grid(row=2, column=1, padx=5, pady=5)

result_labels = [tk.Label(root, text="") for _ in range(6)]
for i, label in enumerate(result_labels):
    label.grid(row=i+3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
