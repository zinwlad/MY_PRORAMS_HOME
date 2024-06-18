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

class RectangleCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Расчет количества прямоугольников на листе бумаги")

        self.paper_size_combobox = ttk.Combobox(root, values=list(PAPER_SIZES.keys()))
        self.paper_size_combobox.grid(row=0, column=1, padx=5, pady=5)
        self.paper_size_combobox.set("Выберите размер бумаги")

        tk.Label(root, text="Длина прямоугольника (мм):").grid(row=1, column=0, padx=5, pady=5)
        self.length_entry = tk.Entry(root)
        self.length_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(root, text="Ширина прямоугольника (мм):").grid(row=2, column=0, padx=5, pady=5)
        self.width_entry = tk.Entry(root)
        self.width_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(root, text="Рассчитать", command=self.calculate_and_display_results).grid(row=3, column=0, padx=5, pady=5)
        tk.Button(root, text="Очистить", command=self.clear_entries).grid(row=3, column=1, padx=5, pady=5)

        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.canvas = tk.Canvas(root, width=450, height=450, bg="white")
        self.canvas.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def validate_numeric_input(self, value: str) -> int:
        try:
            value = int(value)
            if value <= 0:
                raise ValueError("Значение должно быть положительным числом.")
            return value
        except ValueError:
            raise ValueError("Введите корректное числовое значение.")

    def calculate_num_rectangles(self, rect_length: int, rect_width: int, paper_length: int, paper_width: int) -> int:
        if not 0 < rect_length <= paper_length or not 0 < rect_width <= paper_width:
            raise ValueError("Неверные размеры прямоугольника или бумаги.")
        return (paper_width // rect_width) * (paper_length // rect_length)

    def draw_rectangles(self, rect_length, rect_width, paper_length, paper_width):
        self.canvas.delete("all")

        scale = min(self.canvas.winfo_width() / paper_width, self.canvas.winfo_height() / paper_length)
        scaled_paper_width = paper_width * scale
        scaled_paper_length = paper_length * scale
        scaled_rect_width = rect_width * scale
        scaled_rect_length = rect_length * scale

        self.canvas.create_rectangle(0, 0, scaled_paper_width, scaled_paper_length, outline="black")

        for i in range(paper_length // rect_length):
            for j in range(paper_width // rect_width):
                x0 = j * scaled_rect_width
                y0 = i * scaled_rect_length
                x1 = x0 + scaled_rect_width
                y1 = y0 + scaled_rect_length
                self.canvas.create_rectangle(x0, y0, x1, y1, outline="blue")

    def calculate_and_display_results(self):
        try:
            rect_length = self.validate_numeric_input(self.length_entry.get())
            rect_width = self.validate_numeric_input(self.width_entry.get())

            selected_paper_size = self.paper_size_combobox.get()
            if selected_paper_size == "Все размеры":
                result_text = ""
                for name, size in PAPER_SIZES.items():
                    if name in ["Выберите размер бумаги", "Все размеры", "Свой размер"]:
                        continue
                    result = self.calculate_num_rectangles(rect_length, rect_width, *size)
                    result_text += f"{name}: {result}\n"
                self.result_label.config(text=result_text.strip())
            elif selected_paper_size == "Свой размер":
                custom_length = simpledialog.askstring("Пользовательский размер", "Введите длину бумаги (мм):")
                custom_width = simpledialog.askstring("Пользовательский размер", "Введите ширину бумаги (мм):")
                custom_length = self.validate_numeric_input(custom_length)
                custom_width = self.validate_numeric_input(custom_width)
                paper_length, paper_width = custom_length, custom_width
                result = self.calculate_num_rectangles(rect_length, rect_width, paper_length, paper_width)
                self.result_label.config(text=f"Количество прямоугольников: {result}")
                self.draw_rectangles(rect_length, rect_width, paper_length, paper_width)
            elif selected_paper_size in PAPER_SIZES:
                paper_length, paper_width = PAPER_SIZES[selected_paper_size]
                result = self.calculate_num_rectangles(rect_length, rect_width, paper_length, paper_width)
                self.result_label.config(text=f"{selected_paper_size}: {result}")
                self.draw_rectangles(rect_length, rect_width, paper_length, paper_width)
            else:
                raise ValueError("Выберите размер бумаги.")
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))
        except TypeError:
            # Если пользователь закрыл диалоговое окно без ввода данных
            pass

    def clear_entries(self):
        self.length_entry.delete(0, tk.END)
        self.width_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = RectangleCalculatorApp(root)
    root.mainloop()
