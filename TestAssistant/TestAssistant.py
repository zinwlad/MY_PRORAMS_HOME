import tkinter as tk
from tkinter import ttk
from search import SearchFrame  # Предполагая, что SearchFrame определен в модуле search.py
import web_testing

class FontSizeFrame(tk.Frame):
    def __init__(self, parent, tree):
        super().__init__(parent)
        self.tree = tree
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Размер шрифта:").pack(side=tk.LEFT)

        self.scale = tk.Scale(self, from_=6, to=24, orient=tk.HORIZONTAL, command=self.update_font_size)
        self.scale.set(10)  # Установка начального значения
        self.scale.pack(side=tk.LEFT)

    def update_font_size(self, event):
        new_size = int(self.scale.get())
        style = ttk.Style()
        style.configure('Treeview', font=('Helvetica', new_size))
        style.configure('Treeview.Heading', font=('Helvetica', new_size))

def make_columns_movable(tree):
    for col in tree["columns"]:
        tree.heading(col, text=col, command=lambda _col=col: move_column(tree, _col))

def move_column(tree, col):
    cols = list(tree["columns"])
    idx = cols.index(col)
    if idx > 0:
        cols[idx], cols[idx - 1] = cols[idx - 1], cols[idx]
        tree["columns"] = cols
        for item in tree.get_children():
            values = list(tree.item(item, "values"))
            values[idx], values[idx - 1] = values[idx - 1], values[idx]
            tree.item(item, values=values)

def main():
    root = tk.Tk()
    root.title("TestAssistant - Ваш помощник в тестировании")
    root.geometry("800x600")

    # Создаем панель поиска и добавляем ее вверху окна
    search_frame = SearchFrame(root)
    search_frame.pack(fill=tk.X, padx=10, pady=10)

    # Основной контроллер вкладок
    tab_control = ttk.Notebook(root)

    # Создаем вкладки и добавляем их в основной контроллер вкладок
    web_tab = web_testing.create_tabs(root)
    mobile_tab = ttk.Frame(tab_control)
    desktop_tab = ttk.Frame(tab_control)

    tab_control.add(web_tab, text='Веб-тестирование')
    tab_control.add(mobile_tab, text='Мобильное тестирование')
    tab_control.add(desktop_tab, text='Десктопное тестирование')

    tab_control.pack(expand=1, fill='both')

    # Если web_tab содержит Treeview, применяем функцию make_columns_movable
    # Вам нужно изменить этот код, чтобы он соответствовал вашей структуре
    for tab in [web_tab, mobile_tab, desktop_tab]:
        if hasattr(tab, 'treeview'):
            make_columns_movable(tab.treeview)

    root.mainloop()


if __name__ == "__main__":
    main()