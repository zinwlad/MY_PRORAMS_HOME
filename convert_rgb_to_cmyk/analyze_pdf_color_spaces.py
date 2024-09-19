import fitz  # PyMuPDF
import os
import logging

# Настройка логирования
logging.basicConfig(filename='pdf_analysis.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def points_to_mm(points):
    """Преобразует размеры из точек в миллиметры."""
    return points * 25.4 / 72

def analyze_pdf(pdf_path):
    """Анализирует PDF-файл и собирает статистику."""
    if not os.path.isfile(pdf_path):
        print(f"Файл по указанному пути не существует: {pdf_path}")
        return

    try:
        doc = fitz.open(pdf_path)
        logging.info(f"Успешно открыт PDF файл: {pdf_path}")
    except Exception as e:
        print(f"Не удалось открыть PDF-файл: {e}")
        logging.error(f"Не удалось открыть PDF-файл: {e}")
        return

    total_pages = doc.page_count
    rgb_pages = set()
    cmyk_pages = set()
    font_set = set()
    page_sizes_mm = []

    for page_num in range(total_pages):
        try:
            page = doc.load_page(page_num)
        except Exception as e:
            print(f"Не удалось загрузить страницу {page_num + 1}: {e}")
            logging.error(f"Не удалось загрузить страницу {page_num + 1}: {e}")
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
            print(f"Не удалось получить информацию о шрифтах на странице {page_num + 1}: {e}")
            logging.error(f"Не удалось получить информацию о шрифтах на странице {page_num + 1}: {e}")

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
            print(f"Не удалось получить изображения на странице {page_num + 1}: {e}")
            logging.error(f"Не удалось получить изображения на странице {page_num + 1}: {e}")

    doc.close()

    # Определяем общий формат страниц
    if all(size == page_sizes_mm[0] for size in page_sizes_mm):
        page_format = f"{page_sizes_mm[0][0]:.1f} x {page_sizes_mm[0][1]:.1f} мм"
    else:
        page_format = "Разные размеры страниц"

    # Вывод статистики
    print(f"\nКоличество страниц: {total_pages}")
    print(f"Формат страниц: {page_format}")

    print("\nRGB изображения находятся на страницах:")
    if rgb_pages:
        print(", ".join(map(str, sorted(rgb_pages))))
    else:
        print("Нет изображений в RGB цвете.")

    print("\nCMYK изображения находятся на страницах:")
    if cmyk_pages:
        print(", ".join(map(str, sorted(cmyk_pages))))
    else:
        print("Нет изображений в CMYK цвете.")

    print("\nИспользованные шрифты:")
    if font_set:
        for font in sorted(font_set):
            print(f"  - {font}")
    else:
        print("Шрифты отсутствуют или недоступны.")

if __name__ == "__main__":
    pdf_file_path = input("Введите путь к PDF-файлу: ").strip()
    analyze_pdf(pdf_file_path)
