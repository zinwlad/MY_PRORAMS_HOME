import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
from PyPDF2 import PdfReader, PdfWriter
import os


class PDFReverserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Reverser")
        self.root.geometry("400x200")

        self.label = tk.Label(root, text="Перетащите PDF-файл сюда или нажмите 'Выбрать PDF'")
        self.label.pack(pady=10)

        self.open_button = tk.Button(root, text="Выбрать PDF", command=self.open_file)
        self.open_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Сохранить изменённый PDF", command=self.save_file, state=tk.DISABLED)
        self.save_button.pack(pady=5)

        self.status_label = tk.Label(root, text="")
        self.status_label.pack(pady=10)

        self.file_path = None

        # Настроить поддержку Drag-and-Drop
        self.root.drop_target_register(DND_FILES)
        self.root.dnd_bind('<<Drop>>', self.on_drop)

    def open_file(self):
        """Открытие файла через диалоговое окно"""
        try:
            self.file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
            if self.file_path:
                self.update_status(f"Выбран файл: {self.file_path}")
                self.save_button.config(state=tk.NORMAL)
            else:
                self.update_status("Файл не выбран.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось открыть файл:\n{e}")

    def save_file(self):
        """Сохранение изменённого PDF файла"""
        if not self.file_path:
            self.update_status("Ошибка: Файл не выбран")
            return

        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if output_path:
            try:
                self.reverse_pdf_pages(self.file_path, output_path)
                self.update_status(f"Изменённый файл сохранён: {output_path}")
                messagebox.showinfo("Успех", f"Файл успешно сохранён: {output_path}")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Произошла ошибка при обработке файла:\n{e}")

    def reverse_pdf_pages(self, input_pdf_path, output_pdf_path):
        """Реверсирование страниц PDF и сохранение в новый файл"""
        try:
            reader = PdfReader(input_pdf_path)
            writer = PdfWriter()

            for page_num in reversed(range(len(reader.pages))):
                writer.add_page(reader.pages[page_num])

            with open(output_pdf_path, "wb") as output_pdf:
                writer.write(output_pdf)
        except Exception as e:
            raise Exception(f"Ошибка при реверсировании PDF: {e}")

    def on_drop(self, event):
        """Обработка перетаскивания файла в окно"""
        file_path = self.extract_file_path(event.data)
        if file_path and os.path.isfile(file_path):
            self.file_path = file_path
            self.update_status(f"Выбран файл: {self.file_path}")
            self.save_button.config(state=tk.NORMAL)
        else:
            self.update_status("Ошибка: Не удалось загрузить файл")

    def extract_file_path(self, data):
        """Извлечение пути файла из данных DND"""
        if data.startswith('{'):
            data = data.split('}')[0]  # Удаление лишних символов, характерных для некоторых ОС
        return data.replace('{', '').replace('}', '').replace('/', os.sep)

    def update_status(self, message):
        """Обновление статуса на экране"""
        self.status_label.config(text=message)


if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = PDFReverserApp(root)
    root.mainloop()
