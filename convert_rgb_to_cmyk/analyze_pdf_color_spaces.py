import fitz  # PyMuPDF
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def points_to_mm(points):
    """Преобразует размеры из точек в миллиметры."""
    return points * 25.4 / 72

def analyze_pdf(pdf_path):
    """Анализирует PDF-файл и собирает статистику."""
    if not os.path.isfile(pdf_path):
        return f"Файл по указанному пути не существует: {pdf_path}"

    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        return f"Не удалось открыть PDF-файл: {e}"

    total_pages = doc.page_count
    rgb_pages = set()
    cmyk_pages = set()
    font_set = set()
    page_sizes_mm = []

    for page_num in range(total_pages):
        try:
            page = doc.load_page(page_num)
        except Exception as e:
            continue

        page_size = page.rect
        width_mm = points_to_mm(page_size.width)
        height_mm = points_to_mm(page_size.height)
        page_sizes_mm.append((width_mm, height_mm))

        try:
            page_dict = page.get_text("dict")
            if 'fonts' in page_dict:
                fonts = page_dict['fonts']
                for font in fonts:
                    font_name = font['fontname']
                    font_set.add(font_name)
        except Exception as e:
            pass

        try:
            images = page.get_images(full=True)
            if images:
                for img in images:
                    xref = img[0]
                    pix = fitz.Pixmap(doc, xref)
                    if pix.colorspace.n == 3:
                        rgb_pages.add(page_num + 1)
                    elif pix.colorspace.n == 4:
                        cmyk_pages.add(page_num + 1)
        except Exception as e:
            pass

    doc.close()

    # Определяем общий формат страниц
    if all(size == page_sizes_mm[0] for size in page_sizes_mm):
        page_format = f"{page_sizes_mm[0][0]:.1f} x {page_sizes_mm[0][1]:.1f} мм"
    else:
        page_format = "Разные размеры страниц"

    # Формирование результата
    result = []
    result.append(f"Количество страниц: {total_pages}")
    result.append(f"Формат страниц: {page_format}")

    result.append("\nRGB изображения находятся на страницах:")
    if rgb_pages:
        result.append(", ".join(map(str, sorted(rgb_pages))))
    else:
        result.append("Нет изображений в RGB цвете.")

    result.append("\nCMYK изображения находятся на страницах:")
    if cmyk_pages:
        result.append(", ".join(map(str, sorted(cmyk_pages))))
    else:
        result.append("Нет изображений в CMYK цвете.")

    result.append("\nИспользованные шрифты:")
    if font_set:
        for font in sorted(font_set):
            result.append(f"  - {font}")
    else:
        result.append("Шрифты отсутствуют или недоступны.")

    return "\n".join(result)

def browse_file():
    """Открывает диалоговое окно для выбора файла PDF и запускает анализ."""
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        result_text = analyze_pdf(file_path)
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, result_text)

# Создание главного окна
root = tk.Tk()
root.title("Анализатор PDF")

# Создание и размещение элементов интерфейса
open_button = tk.Button(root, text="Выбрать PDF файл", command=browse_file)
open_button.pack(pady=10)

text_area = tk.Text(root, wrap=tk.WORD, height=20, width=80)
text_area.pack(padx=10, pady=10)

# Запуск основного цикла
root.mainloop()
