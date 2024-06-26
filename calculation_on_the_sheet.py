import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

class RectangleCalculatorApp:
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

    def __init__(self, root):
        self.root = root
        self.root.title("Расчет количества прямоугольников на листе бумаги")
        self.root.minsize(600, 400)

        self.create_widgets()

    def create_widgets(self):
        # Группировка элементов в LabelFrame
        frame = ttk.LabelFrame(self.root, text="Параметры прямоугольника и бумаги")
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.paper_size_combobox = ttk.Combobox(frame, values=list(self.PAPER_SIZES.keys()))
        self.paper_size_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.paper_size_combobox.set("Выберите размер бумаги")

        tk.Label(frame, text="Длина прямоугольника (мм):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.length_entry = tk.Entry(frame)
        self.length_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        tk.Label(frame, text="Ширина прямоугольника (мм):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.width_entry = tk.Entry(frame)
        self.width_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        tk.Button(frame, text="Рассчитать", command=self.calculate_and_display_results).grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        tk.Button(frame, text="Очистить", command=self.clear_entries).grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        self.result_label = tk.Label(frame, text="", wraplength=400, justify="left")
        self.result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        self.canvas = tk.Canvas(self.root, width=450, height=450, bg="white")
        self.canvas.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.canvas.bind("<Configure>", self.draw_on_canvas)

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def validate_numeric_input(self, value: str) -> int:
        if not value.strip():  # Если строка пустая или состоит только из пробелов
            raise ValueError("Введите числовое значение.")
        try:
            numeric_value = int(value)
            if numeric_value <= 0:
                raise ValueError("Значение должно быть положительным числом.")
            return numeric_value
        except ValueError:
            raise ValueError("Введите корректное числовое значение.")

    def calculate_num_rectangles(self, rect_length: int, rect_width: int, paper_length: int, paper_width: int) -> int:
        if not 0 < rect_length <= paper_length or not 0 < rect_width <= paper_width:
            raise ValueError("Неверные размеры прямоугольника или бумаги.")
        return (paper_width // rect_width) * (paper_length // rect_length)

    def draw_on_canvas(self, event=None):
        self.canvas.delete("all")
        paper_size = self.get_selected_paper_size()

        if paper_size == "Все размеры":
            return

        length_entry_value = self.length_entry.get().strip()
        width_entry_value = self.width_entry.get().strip()

        if not length_entry_value or not width_entry_value:
            return

        try:
            rect_length = self.validate_numeric_input(length_entry_value)
            rect_width = self.validate_numeric_input(width_entry_value)

            if paper_size and paper_size in self.PAPER_SIZES:
                paper_length, paper_width = self.PAPER_SIZES[paper_size]

                scale = min(self.canvas.winfo_width() / paper_width, self.canvas.winfo_height() / paper_length)
                margin_x = (self.canvas.winfo_width() - paper_width * scale) / 2
                margin_y = (self.canvas.winfo_height() - paper_length * scale) / 2
                scaled_rect_width = rect_width * scale
                scaled_rect_length = rect_length * scale

                for i in range(paper_length // rect_length):
                    for j in range(paper_width // rect_width):
                        x0 = margin_x + j * scaled_rect_width
                        y0 = margin_y + i * scaled_rect_length
                        x1 = x0 + scaled_rect_width
                        y1 = y0 + scaled_rect_length
                        self.canvas.create_rectangle(x0, y0, x1, y1, outline="blue")
                self.canvas.create_rectangle(margin_x, margin_y, margin_x + paper_width * scale, margin_y + paper_length * scale, outline="black")

            else:
                messagebox.showerror("Ошибка", "Выберите корректный размер бумаги.")
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def calculate_and_display_results(self):
        try:
            rect_length = self.validate_numeric_input(self.length_entry.get())
            rect_width = self.validate_numeric_input(self.width_entry.get())
            paper_size = self.get_selected_paper_size()

            if paper_size == "Все размеры":
                result_text = ""
                for name, size in self.PAPER_SIZES.items():
                    if name in ["Выберите размер бумаги", "Все размеры", "Свой размер"]:
                        continue
                    result = self.calculate_num_rectangles(rect_length, rect_width, *size)
                    result_text += f"{name}: {result}\n"
                self.result_label.config(text=result_text.strip())
            elif paper_size == "Свой размер":
                custom_length = simpledialog.askstring("Пользовательский размер", "Введите длину бумаги (мм):")
                custom_width = simpledialog.askstring("Пользовательский размер", "Введите ширину бумаги (мм):")
                if custom_length is not None and custom_width is not None:
                    custom_length = self.validate_numeric_input(custom_length)
                    custom_width = self.validate_numeric_input(custom_width)
                    paper_length, paper_width = custom_length, custom_width
                    result = self.calculate_num_rectangles(rect_length, rect_width, paper_length, paper_width)
                    self.result_label.config(text=f"Количество прямоугольников: {result}")
                    self.draw_on_canvas()
            elif paper_size in self.PAPER_SIZES:
                paper_length, paper_width = self.PAPER_SIZES[paper_size]
                result = self.calculate_num_rectangles(rect_length, rect_width, paper_length, paper_width)
                self.result_label.config(text=f"{paper_size}: {result}")
                self.draw_on_canvas()
            else:
                raise ValueError("Выберите размер бумаги.")
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def clear_entries(self):
        self.length_entry.delete(0, tk.END)
        self.width_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.canvas.delete("all")
        self.paper_size_combobox.set("Выберите размер бумаги")

    def get_selected_paper_size(self) -> str:
        return self.paper_size_combobox.get()


if __name__ == "__main__":
    root = tk.Tk()
    app = RectangleCalculatorApp(root)
    root.mainloop()
