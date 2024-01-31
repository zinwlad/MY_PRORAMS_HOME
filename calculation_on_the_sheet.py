import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

PAPER_SIZES = {
    "Выберите размер бумаги": None,
    "Все размеры": "Special",
    "Свой размер": "Custom",
    "A4 горизонтально": (297, 210),
    "A4 вертикально": (210, 297),
    "A3 горизонтально": (420, 297),
    "A3 вертикально": (297, 420),
    "SRA3 горизонтально": (450, 320),
    "SRA3 вертикально": (320, 450),
}

def validate_numeric_input(value):
    try:
        value = int(value)
        if value <= 0:
            raise ValueError("Значение должно быть положительным числом.")
        return value
    except ValueError:
        raise ValueError("Введите корректное числовое значение.")

def calculate_num_rectangles(rect_length, rect_width, paper_length, paper_width):
    if not 0 < rect_length <= paper_length or not 0 < rect_width <= paper_width:
        raise ValueError("Неверные размеры прямоугольника или бумаги.")
    return (paper_width // rect_width) * (paper_length // rect_length)

def calculate_and_display_results():
    try:
        rect_length = validate_numeric_input(length_entry.get())
        rect_width = validate_numeric_input(width_entry.get())

        selected_paper_size = paper_size_combobox.get()
        if selected_paper_size == "Все размеры":
            result_text = ""
            for name, size in PAPER_SIZES.items():
                if name in ["Выберите размер бумаги", "Все размеры", "Свой размер"]:
                    continue
                result = calculate_num_rectangles(rect_length, rect_width, *size)
                result_text += f"{name}: {result}\n"
            result_label.config(text=result_text.strip())
        elif selected_paper_size == "Свой размер":
            custom_length = simpledialog.askstring("Пользовательский размер", "Введите длину бумаги (мм):")
            custom_width = simpledialog.askstring("Пользовательский размер", "Введите ширину бумаги (мм):")
            custom_length = validate_numeric_input(custom_length)
            custom_width = validate_numeric_input(custom_width)
            paper_length, paper_width = custom_length, custom_width
            result = calculate_num_rectangles(rect_length, rect_width, paper_length, paper_width)
            result_label.config(text=f"Количество прямоугольников: {result}")
        elif selected_paper_size in PAPER_SIZES:
            paper_length, paper_width = PAPER_SIZES[selected_paper_size]
            result = calculate_num_rectangles(rect_length, rect_width, paper_length, paper_width)
            result_label.config(text=f"{selected_paper_size}: {result}")
        else:
            raise ValueError("Выберите размер бумаги.")
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))
    except TypeError:
        # Если пользователь закрыл диалоговое окно без ввода данных
        pass

def clear_entries():
    length_entry.delete(0, tk.END)
    width_entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Расчет количества прямоугольников на листе бумаги")

paper_size_combobox = ttk.Combobox(root, values=list(PAPER_SIZES.keys()))
paper_size_combobox.grid(row=0, column=1, padx=5, pady=5)
paper_size_combobox.set("Выберите размер бумаги")

length_entry = tk.Entry(root)
length_entry.grid(row=1, column=1, padx=5, pady=5)
tk.Label(root, text="Длина прямоугольника (мм):").grid(row=1, column=0, padx=5, pady=5)

width_entry = tk.Entry(root)
width_entry.grid(row=2, column=1, padx=5, pady=5)
tk.Label(root, text="Ширина прямоугольника (мм):").grid(row=2, column=0, padx=5, pady=5)

calculate_button = tk.Button(root, text="Рассчитать", command=calculate_and_display_results)
calculate_button.grid(row=3, column=0, padx=5, pady=5)

clear_button = tk.Button(root, text="Очистить", command=clear_entries)
clear_button.grid(row=3, column=1, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
