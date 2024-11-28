import tkinter as tk
from tkinter import messagebox, simpledialog, ttk, filedialog
import json
from reportlab.pdfgen import canvas as pdf_canvas
from reportlab.lib.units import mm
import os

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

UNITS = {
    "мм": 1,
    "см": 10,
    "дюймы": 25.4
}

DEFAULT_TEMPLATE = {
    "name": "",
    "rect_length": 0,
    "rect_width": 0,
    "paper_size": "",
    "spacing": 0,
    "quantity": 1,
    "units": "мм"
}


class RectangleCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Расчет количества прямоугольников на листе бумаги")

        # Создаем фреймы для организации интерфейса
        self.input_frame = ttk.LabelFrame(root, text="Параметры")
        self.input_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.template_frame = ttk.LabelFrame(root, text="Шаблоны")
        self.template_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        self.result_frame = ttk.LabelFrame(root, text="Результаты")
        self.result_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Основные параметры
        ttk.Label(self.input_frame, text="Размер бумаги:").grid(row=0, column=0, padx=5, pady=5)
        self.paper_size_combobox = ttk.Combobox(self.input_frame, values=list(PAPER_SIZES.keys()))
        self.paper_size_combobox.grid(row=0, column=1, padx=5, pady=5)
        self.paper_size_combobox.set("Выберите размер бумаги")

        # Единицы измерения
        ttk.Label(self.input_frame, text="Единицы измерения:").grid(row=1, column=0, padx=5, pady=5)
        self.units_var = tk.StringVar(value="мм")
        self.units_combobox = ttk.Combobox(self.input_frame, values=list(UNITS.keys()), textvariable=self.units_var)
        self.units_combobox.grid(row=1, column=1, padx=5, pady=5)

        # Размеры прямоугольника
        ttk.Label(self.input_frame, text="Длина:").grid(row=2, column=0, padx=5, pady=5)
        self.length_entry = ttk.Entry(self.input_frame)
        self.length_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.input_frame, text="Ширина:").grid(row=3, column=0, padx=5, pady=5)
        self.width_entry = ttk.Entry(self.input_frame)
        self.width_entry.grid(row=3, column=1, padx=5, pady=5)

        # Расстояние между листами
        ttk.Label(self.input_frame, text="Расстояние между:").grid(row=4, column=0, padx=5, pady=5)
        self.spacing_entry = ttk.Entry(self.input_frame)
        self.spacing_entry.grid(row=4, column=1, padx=5, pady=5)
        self.spacing_entry.insert(0, "0")

        # Количество
        ttk.Label(self.input_frame, text="Тираж:").grid(row=5, column=0, padx=5, pady=5)
        self.quantity_entry = ttk.Entry(self.input_frame)
        self.quantity_entry.grid(row=5, column=1, padx=5, pady=5)
        self.quantity_entry.insert(0, "1")

        # Кнопки управления
        self.buttons_frame = ttk.Frame(self.input_frame)
        self.buttons_frame.grid(row=6, column=0, columnspan=2, pady=10)

        ttk.Button(self.buttons_frame, text="Рассчитать", command=self.calculate_and_display_results).grid(row=0,
                                                                                                           column=0,
                                                                                                           padx=5)
        ttk.Button(self.buttons_frame, text="Очистить", command=self.clear_entries).grid(row=0, column=1, padx=5)
        ttk.Button(self.buttons_frame, text="Экспорт в PDF", command=self.export_to_pdf).grid(row=0, column=2, padx=5)

        # Шаблоны
        self.templates = self.load_templates()
        self.template_listbox = tk.Listbox(self.template_frame, height=10)
        self.template_listbox.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.update_template_list()

        ttk.Button(self.template_frame, text="Сохранить как шаблон", command=self.save_template).grid(row=1, column=0,
                                                                                                      padx=5, pady=5)
        ttk.Button(self.template_frame, text="Загрузить шаблон", command=self.load_template).grid(row=1, column=1,
                                                                                                  padx=5, pady=5)
        ttk.Button(self.template_frame, text="Удалить шаблон", command=self.delete_template).grid(row=2, column=0,
                                                                                                  columnspan=2, padx=5,
                                                                                                  pady=5)

        # Результаты
        self.result_label = ttk.Label(self.result_frame, text="")
        self.result_label.grid(row=0, column=0, padx=5, pady=5)

        self.canvas = tk.Canvas(self.result_frame, width=450, height=450, bg="white")
        self.canvas.grid(row=1, column=0, padx=5, pady=5)

        # Настройка расширяемости grid
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)

    def validate_numeric_input(self, value: str) -> int:
        try:
            value = int(value)
            if value <= 0:
                raise ValueError("Значение должно быть положительным числом.")
            return value
        except ValueError:
            raise ValueError("Введите корректное числовое значение.")

    def convert_to_mm(self, value: float, unit: str) -> float:
        return value * UNITS[unit]

    def convert_from_mm(self, value: float, unit: str) -> float:
        return value / UNITS[unit]

    def calculate_num_rectangles(self, rect_length: float, rect_width: float,
                                 paper_length: float, paper_width: float,
                                 spacing: float = 0) -> tuple:
        if not 0 < rect_length <= paper_length or not 0 < rect_width <= paper_width:
            raise ValueError("Неверные размеры прямоугольника или бумаги.")

        # Учитываем расстояние между прямоугольниками
        effective_width = rect_width + spacing
        effective_length = rect_length + spacing

        # Вычисляем количество прямоугольников по каждой оси
        num_width = int(paper_width / effective_width)
        num_length = int(paper_length / effective_length)

        return num_width * num_length, (num_width, num_length)

    def draw_rectangles(self, rect_length, rect_width, paper_length, paper_width, spacing=0):
        self.canvas.delete("all")

        # Вычисляем масштаб
        scale = min(self.canvas.winfo_width() / paper_width,
                    self.canvas.winfo_height() / paper_length)

        scaled_paper_width = paper_width * scale
        scaled_paper_length = paper_length * scale
        scaled_rect_width = rect_width * scale
        scaled_rect_length = rect_length * scale
        scaled_spacing = spacing * scale

        # Рисуем лист бумаги
        self.canvas.create_rectangle(0, 0, scaled_paper_width, scaled_paper_length,
                                     outline="black", width=2)

        # Вычисляем количество прямоугольников
        _, (num_width, num_length) = self.calculate_num_rectangles(
            rect_length, rect_width, paper_length, paper_width, spacing)

        # Рисуем прямоугольники с учетом расстояния между ними
        for i in range(num_length):
            for j in range(num_width):
                x0 = j * (scaled_rect_width + scaled_spacing)
                y0 = i * (scaled_rect_length + scaled_spacing)
                x1 = x0 + scaled_rect_width
                y1 = y0 + scaled_rect_length
                self.canvas.create_rectangle(x0, y0, x1, y1, outline="blue")

    def calculate_and_display_results(self):
        try:
            # Получаем значения и конвертируем их в мм
            current_unit = self.units_var.get()
            rect_length = self.convert_to_mm(float(self.length_entry.get()), current_unit)
            rect_width = self.convert_to_mm(float(self.width_entry.get()), current_unit)
            spacing = self.convert_to_mm(float(self.spacing_entry.get()), current_unit)
            quantity = int(self.quantity_entry.get())

            selected_paper_size = self.paper_size_combobox.get()
            if selected_paper_size == "Все размеры":
                result_text = ""
                for name, size in PAPER_SIZES.items():
                    if name in ["Выберите размер бумаги", "Все размеры", "Свой размер"]:
                        continue
                    total_rect, _ = self.calculate_num_rectangles(
                        rect_length, rect_width, size[0], size[1], spacing)
                    sheets_needed = (quantity + total_rect - 1) // total_rect
                    result_text += f"{name}: {total_rect} шт. на листе, "
                    result_text += f"нужно листов: {sheets_needed}\n"
                self.result_label.config(text=result_text.strip())
            elif selected_paper_size == "Свой размер":
                custom_length = self.convert_to_mm(
                    float(simpledialog.askstring("Пользовательский размер",
                                                 f"Введите длину бумаги ({current_unit}):")),
                    current_unit)
                custom_width = self.convert_to_mm(
                    float(simpledialog.askstring("Пользовательский размер",
                                                 f"Введите ширину бумаги ({current_unit}):")),
                    current_unit)
                total_rect, _ = self.calculate_num_rectangles(
                    rect_length, rect_width, custom_length, custom_width, spacing)
                sheets_needed = (quantity + total_rect - 1) // total_rect
                result_text = f"Количество прямоугольников на листе: {total_rect}\n"
                result_text += f"Необходимо листов: {sheets_needed}"
                self.result_label.config(text=result_text)
                self.draw_rectangles(rect_length, rect_width, custom_length, custom_width, spacing)
            elif selected_paper_size in PAPER_SIZES:
                paper_length, paper_width = PAPER_SIZES[selected_paper_size]
                total_rect, _ = self.calculate_num_rectangles(
                    rect_length, rect_width, paper_length, paper_width, spacing)
                sheets_needed = (quantity + total_rect - 1) // total_rect
                result_text = f"{selected_paper_size}:\n"
                result_text += f"Количество на листе: {total_rect}\n"
                result_text += f"Необходимо листов: {sheets_needed}"
                self.result_label.config(text=result_text)
                self.draw_rectangles(rect_length, rect_width, paper_length, paper_width, spacing)
            else:
                raise ValueError("Выберите размер бумаги.")
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))
        except TypeError:
            pass

    def clear_entries(self):
        self.length_entry.delete(0, tk.END)
        self.width_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.canvas.delete("all")

    def load_templates(self):
        try:
            with open("templates.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def update_template_list(self):
        self.template_listbox.delete(0, tk.END)
        for template in self.templates.values():
            self.template_listbox.insert(tk.END, template["name"])

    def save_template(self):
        template_name = simpledialog.askstring("Сохранить шаблон", "Введите имя шаблона:")
        if template_name:
            template = {
                "name": template_name,
                "rect_length": int(self.length_entry.get()),
                "rect_width": int(self.width_entry.get()),
                "paper_size": self.paper_size_combobox.get(),
                "spacing": int(self.spacing_entry.get()),
                "quantity": int(self.quantity_entry.get()),
                "units": self.units_var.get()
            }
            self.templates[template_name] = template
            with open("templates.json", "w") as file:
                json.dump(self.templates, file)
            self.update_template_list()

    def load_template(self):
        selected_index = self.template_listbox.curselection()
        if selected_index:
            template_name = self.template_listbox.get(selected_index)
            template = self.templates[template_name]
            self.length_entry.delete(0, tk.END)
            self.length_entry.insert(0, template["rect_length"])
            self.width_entry.delete(0, tk.END)
            self.width_entry.insert(0, template["rect_width"])
            self.paper_size_combobox.set(template["paper_size"])
            self.spacing_entry.delete(0, tk.END)
            self.spacing_entry.insert(0, template["spacing"])
            self.quantity_entry.delete(0, tk.END)
            self.quantity_entry.insert(0, template["quantity"])
            self.units_var.set(template["units"])

    def delete_template(self):
        selected_index = self.template_listbox.curselection()
        if selected_index:
            template_name = self.template_listbox.get(selected_index)
            del self.templates[template_name]
            with open("templates.json", "w") as file:
                json.dump(self.templates, file)
            self.update_template_list()

    def export_to_pdf(self):
        try:
            # Получаем текущие значения
            current_unit = self.units_var.get()
            rect_length = self.convert_to_mm(float(self.length_entry.get()), current_unit)
            rect_width = self.convert_to_mm(float(self.width_entry.get()), current_unit)
            spacing = self.convert_to_mm(float(self.spacing_entry.get()), current_unit)
            quantity = int(self.quantity_entry.get())

            # Получаем размер бумаги
            selected_paper_size = self.paper_size_combobox.get()
            if selected_paper_size not in PAPER_SIZES or selected_paper_size in ["Выберите размер бумаги",
                                                                                 "Все размеры"]:
                raise ValueError("Выберите конкретный размер бумаги для экспорта в PDF")

            if selected_paper_size == "Свой размер":
                paper_length = self.convert_to_mm(
                    float(simpledialog.askstring("Размер бумаги",
                                                 f"Введите длину бумаги ({current_unit}):")),
                    current_unit)
                paper_width = self.convert_to_mm(
                    float(simpledialog.askstring("Размер бумаги",
                                                 f"Введите ширину бумаги ({current_unit}):")),
                    current_unit)
            else:
                paper_length, paper_width = PAPER_SIZES[selected_paper_size]

            # Создаем PDF файл
            filename = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf")],
                title="Сохранить PDF"
            )

            if filename:
                # Создаем PDF документ
                c = pdf_canvas.Canvas(filename, pagesize=(paper_width * mm, paper_length * mm))

                # Рисуем прямоугольники
                total_rect, (num_width, num_length) = self.calculate_num_rectangles(
                    rect_length, rect_width, paper_length, paper_width, spacing)

                for i in range(num_length):
                    for j in range(num_width):
                        x = j * (rect_width + spacing)
                        y = paper_length - (i + 1) * (rect_length + spacing)
                        c.rect(x * mm, y * mm, rect_width * mm, rect_length * mm)

                # Добавляем информацию о раскладке
                c.setFont("Helvetica", 10)
                info_text = [
                    f"Размер листа: {paper_width}x{paper_length} мм",
                    f"Размер прямоугольника: {rect_width}x{rect_length} мм",
                    f"Расстояние между: {spacing} мм",
                    f"Количество на листе: {total_rect}",
                    f"Тираж: {quantity}",
                    f"Необходимо листов: {(quantity + total_rect - 1) // total_rect}"
                ]

                for i, text in enumerate(info_text):
                    c.drawString(5 * mm, (5 + i * 5) * mm, text)

                c.save()
                messagebox.showinfo("Успех", "PDF файл успешно создан!")

        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))
        except TypeError:
            pass


if __name__ == "__main__":
    root = tk.Tk()
    app = RectangleCalculatorApp(root)
    root.mainloop()
