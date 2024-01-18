import tkinter as tk
import re

class SearchFrame(tk.Frame):
    def __init__(self, parent, tree=None):
        super().__init__(parent)
        self.tree = tree
        self.create_widgets()

    def create_widgets(self):
        self.search_entry = tk.Entry(self)
        self.search_entry.pack(side=tk.LEFT, padx=(0, 10))

        self.search_button = tk.Button(self, text="Поиск", command=self.perform_search)
        self.search_button.pack(side=tk.LEFT)

    def perform_search(self):
        search_query = self.search_entry.get()
        self.search_in_treeview(self.tree, search_query)

    def search_in_treeview(self, tree, query):
        """ Функция для поиска в Treeview с использованием регулярных выражений. """
        if tree is not None:
            pattern = re.compile(query, re.IGNORECASE)
            for item in tree.get_children():
                values = " ".join(tree.item(item, 'values'))
                if pattern.search(values):
                    tree.item(item, tags=('found',))
                else:
                    tree.item(item, tags=())
            self.highlight_search_results(tree)

    def highlight_search_results(self, tree):
        """ Функция для подсветки результатов поиска. """
        tree.tag_configure('found', background='yellow')

    def update_treeview(self, tree):
        """ Обновляет Treeview для поиска. """
        self.tree = tree

def treeview_sort_column(tree, col, reverse):
    """ Функция сортировки для Treeview. """
    l = [(tree.set(k, col), k) for k in tree.get_children('')]
    try:
        l.sort(key=lambda t: float(t[0]), reverse=reverse)
    except ValueError:
        l.sort(key=lambda t: t[0], reverse=reverse)
    for index, (val, k) in enumerate(l):
        tree.move(k, '', index)
    tree.heading(col, command=lambda _col=col: treeview_sort_column(tree, _col, not reverse))

# Далее, используйте функцию treeview_sort_column при создании столбцов Treeview
