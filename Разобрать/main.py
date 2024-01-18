import tkinter as tk
from tkinter import messagebox


def A4Vertical(rect_length, rect_width, paper_length=210, paper_width=297):
    # if rect_length <= 0 or rect_width <= 0:
    #     raise ValueError("Длина и ширина прямоугольника должны быть положительными числами.")
    # if rect_length > paper_length or rect_width > paper_width:
    #     raise ValueError("Размеры прямоугольника превышают размеры листа A4.")

    num_rows = paper_width // rect_width
    num_cols = paper_length // rect_length
    num_rects = num_rows * num_cols

    return num_rects


def A4Horizontal(rect_length, rect_width, paper_length=297, paper_width=210):
    # if rect_length <= 0 or rect_width <= 0:
    #     raise ValueError("Длина и ширина прямоугольника должны быть положительными числами.")
    # if rect_length > paper_length or rect_width > paper_width:
    #     raise ValueError("Размеры прямоугольника превышают размеры листа A4.")

    num_rows = paper_length // rect_length
    num_cols = paper_width // rect_width
    num_rects = num_rows * num_cols

    return num_rects


def A3Vertical(rect_length, rect_width, paper_length=297, paper_width=420):
    if rect_length <= 0 or rect_width <= 0:
        raise ValueError("Длина и ширина прямоугольника должны быть положительными числами.")
    if rect_length > paper_length or rect_width > paper_width:
        raise ValueError("Размеры прямоугольника превышают размеры листа A3.")

    num_rows = paper_width // rect_width
    num_cols = paper_length // rect_length
    num_rects = num_rows * num_cols

    return num_rects


def A3Horizontal(rect_length, rect_width, paper_length=420, paper_width=297):
    if rect_length <= 0 or rect_width <= 0:
        raise ValueError("Длина и ширина прямоугольника должны быть положительными числами.")
    if rect_length > paper_length or rect_width > paper_width:
        raise ValueError("Размеры прямоугольника превышают размеры листа A3.")

    num_rows = paper_length // rect_length
    num_cols = paper_width // rect_width
    num_rects = num_rows * num_cols

    return num_rects


def SRA3Vertical(rect_length, rect_width, paper_length=320, paper_width=450):
    if rect_length <= 0 or rect_width <= 0:
        raise ValueError("Длина и ширина прямоугольника должны быть положительными числами.")
    if rect_length > paper_length or rect_width > paper_width:
        raise ValueError("Размеры прямоугольника превышают размеры листа A3.")

    num_rows = paper_width // rect_width
    num_cols = paper_length // rect_length
    num_rects = num_rows * num_cols

    return num_rects


def SRA3Horizontal(rect_length, rect_width, paper_length=450, paper_width=320):
    if rect_length <= 0 or rect_width <= 0:
        raise ValueError("Длина и ширина прямоугольника должны быть положительными числами.")
    if rect_length > paper_length or rect_width > paper_width:
        raise ValueError("Размеры прямоугольника превышают размеры листа A3.")

    num_rows = paper_length // rect_length
    num_cols = paper_width // rect_width
    num_rects = num_rows * num_cols

    return num_rects


def calculate_rects():
    try:
        rect_length = int(length_entry.get())
        rect_width = int(width_entry.get())

        a4_horizontal_rects = A4Horizontal(rect_length, rect_width)
        a4_vertical_rects = A4Vertical(rect_length, rect_width)
        a3_horizontal_rects = A3Horizontal(rect_length, rect_width)
        a3_vertical_rects = A3Vertical(rect_length, rect_width)
        sra3_horizontal_rects = SRA3Horizontal(rect_length, rect_width)
        sra3_vertical_rects = SRA3Vertical(rect_length, rect_width)

        horizontal_result.config(text=f"Количество прямоугольников на листе A4 (горизонтально): {a4_horizontal_rects}")
        vertical_result.config(text=f"Количество прямоугольников на листе A4 (вертикально): {a4_vertical_rects}")
        horizontal_result_a3.config(text=f"Количество прямоугольников на листе A3 (горизонтально): {a3_horizontal_rects}")
        vertical_result_a3.config(text=f"Количество прямоугольников на листе A3 (вертикально): {a3_vertical_rects}")
        horizontal_result_sra3.config(text=f"Количество прямоугольников на листе SRA3 (горизонтально): {sra3_horizontal_rects}")
        vertical_result_sra3.config(text=f"Количество прямоугольников на листе SRA3 (вертикально): {sra3_vertical_rects}")

    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))


# Создание графического интерфейса
root = tk.Tk()
root.title("Расчет количества прямоугольников на листе A4 и А3")

# Создание текстовых меток и полей для ввода данных
length_label = tk.Label(root, text="Длина прямоугольника (мм):")
length_label.grid(row=0, column=0, padx=5, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=5, pady=5)

width_label = tk.Label(root, text="Ширина прямоугольника (мм):")
width_label.grid(row=1, column=0, padx=5, pady=5)
width_entry = tk.Entry(root)
width_entry.grid(row=1, column=1, padx=10, pady=10)

#a3_vertical_rects = A3Vertical(rect_length, rect_width)

# Создание текстовых меток и полей для ввода данных
length_label = tk.Label(root, text="Длина прямоугольника (мм):")
length_label.grid(row=0, column=0, padx=5, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=5, pady=5)

width_label = tk.Label(root, text="Ширина прямоугольника (мм):")
width_label.grid(row=1, column=0, padx=5, pady=5)
width_entry = tk.Entry(root)
width_entry.grid(row=1, column=1, padx=10, pady=10)

# Создание кнопки для расчета
calculate_button = tk.Button(root, text="Рассчитать", command=calculate_rects)
calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Создание текстовых меток для вывода результатов
horizontal_result = tk.Label(root, text="")
horizontal_result.grid(row=3, column=0, padx=5, pady=5)

vertical_result = tk.Label(root, text="")
vertical_result.grid(row=4, column=0, padx=5, pady=5)

horizontal_result_a3 = tk.Label(root, text="")
horizontal_result_a3.grid(row=5, column=0, padx=5, pady=5)

vertical_result_a3 = tk.Label(root, text="")
vertical_result_a3.grid(row=6, column=0, padx=5, pady=5)

horizontal_result_sra3 = tk.Label(root, text="")
horizontal_result_sra3.grid(row=7, column=0, padx=5, pady=5)

vertical_result_sra3 = tk.Label(root, text="")
vertical_result_sra3.grid(row=8, column=0, padx=5, pady=5)

root.mainloop()