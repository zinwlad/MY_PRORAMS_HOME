import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Для раскрывающегося списка (combobox)

# Константы размеров бумаги
PAPER_SIZES = {
    "Все размеры": "Special",  # Добавляем опцию "Особый"
    "A4 горизонтально": (297, 210),
    "A4 вертикально": (210, 297),
    "A3 горизонтально": (420, 297),
    "A3 вертикально": (297, 420),
    "SRA3 горизонтально": (450, 320),
    "SRA3 вертикально": (320, 450)
}


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

        selected_paper_size = paper_size_combobox.get()
        if selected_paper_size == "Все размеры":
            result_text = ""
            for name, sizes in PAPER_SIZES.items():
                if name == "Все размеры":
                    continue
                result = calculate_num_rectangles(rect_length, rect_width, *sizes)
                result_text += f"{name}: {result}\n"
            result_label.config(text=result_text.strip())
        else:
            paper_length, paper_width = PAPER_SIZES[selected_paper_size]
            result = calculate_num_rectangles(rect_length, rect_width, paper_length, paper_width)
            result_label.config(text=f"Количество прямоугольников на листе {selected_paper_size}: {result}")
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))
    except TypeError:
        messagebox.showerror("Ошибка", "Введите корректные числа.")


def clear_entries():
    length_entry.delete(0, tk.END)
    width_entry.delete(0, tk.END)
    result_label.config(text="")


def create_label_entry_pair(text, row):
    label = tk.Label(root, text=text)
    label.grid(row=row, column=0, padx=5, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=row, column=1, padx=5, pady=5)
    return entry


root = tk.Tk()
root.title("Расчет количества прямоугольников на листе бумаги")

paper_size_combobox = ttk.Combobox(root, values=list(PAPER_SIZES.keys()))
paper_size_combobox.grid(row=0, column=1, padx=5, pady=5)
paper_size_combobox.set("Выберите размер бумаги")

length_entry = create_label_entry_pair("Длина прямоугольника (мм):", 1)
width_entry = create_label_entry_pair("Ширина прямоугольника (мм):", 2)

calculate_button = tk.Button(root, text="Рассчитать", command=calculate_and_display_results)
calculate_button.grid(row=3, column=0, padx=5, pady=5)

clear_button = tk.Button(root, text="Очистить", command=clear_entries)
clear_button.grid(row=3, column=1, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
