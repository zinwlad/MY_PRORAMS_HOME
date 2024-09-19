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
        self.file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.file_path:
            self.status_label.config(text=f"Выбран файл: {self.file_path}")
            self.save_button.config(state=tk.NORMAL)

    def save_file(self):
        if not self.file_path:
            self.status_label.config(text="Ошибка: Файл не выбран")
            return

        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if output_path:
            try:
                self.reverse_pdf_pages(self.file_path, output_path)
                self.status_label.config(text=f"Изменённый файл сохранён: {output_path}")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Произошла ошибка при обработке файла:\n{e}")

    def reverse_pdf_pages(self, input_pdf_path, output_pdf_path):
        reader = PdfReader(input_pdf_path)
        writer = PdfWriter()

        for page_num in reversed(range(len(reader.pages))):
            writer.add_page(reader.pages[page_num])

        with open(output_pdf_path, "wb") as output_pdf:
            writer.write(output_pdf)

    def on_drop(self, event):
        file_path = self.extract_file_path(event.data)
        if file_path and os.path.isfile(file_path):
            self.file_path = file_path
            self.status_label.config(text=f"Выбран файл: {self.file_path}")
            self.save_button.config(state=tk.NORMAL)
        else:
            self.status_label.config(text="Ошибка: Не удалось загрузить файл")

    def extract_file_path(self, data):
        # В зависимости от системы, формат строки может быть разным
        if data.startswith('{'):
            data = data.split('}')[0]  # Вырезать лишние символы
        return data.replace('{', '').replace('}', '').replace('/', '\\')

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = PDFReverserApp(root)
    root.mainloop()
