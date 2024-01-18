# web_testing.py

import tkinter as tk
from tkinter import ttk
from utility_functions import load_data_from_excel

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

def create_movable_treeview(parent, headers, data_list):
    data_tab = ttk.Frame(parent)
    headers = [h for h in headers if h is not None]

    style = ttk.Style()
    style.configure('Treeview', font=('Helvetica', 8))
    style.configure('Treeview.Heading', font=('Helvetica', 8))

    data_table = ttk.Treeview(data_tab, columns=headers, show='headings', style='Treeview')
    for header in headers:
        data_table.heading(header, text=header)
        data_table.column(header, anchor=tk.W, width=100)
    for item in data_list:
        values = [item.get(header, '') for header in headers]
        data_table.insert('', tk.END, values=values)

    scrollbar = ttk.Scrollbar(data_tab, orient='horizontal', command=data_table.xview)
    data_table.configure(xscrollcommand=scrollbar.set)
    scrollbar.pack(side='bottom', fill='x')
    data_table.pack(expand=True, fill='both')

    make_columns_movable(data_table)

    return data_tab, data_table

def create_tab_with_sheets(parent, file_path, style):
    notebook = ttk.Notebook(parent, style=style)
    file_data = load_data_from_excel(file_path)
    for sheet_name, (headers, data_list) in file_data.items():
        tab, _ = create_movable_treeview(notebook, headers, data_list)
        notebook.add(tab, text=sheet_name)
    return notebook

def create_tabs(root):
    style = ttk.Style()
    style.configure('Vertical.TNotebook.Tab', padding=[2, 2], font=('Helvetica', 6))
    style.configure('Vertical.TNotebook', tabposition='wn')

    tab_control = ttk.Notebook(root)

    test_cases_notebook = create_tab_with_sheets(tab_control, 'data/web_data/test_cases.xlsx', 'Vertical.TNotebook')
    bug_reports_notebook = create_tab_with_sheets(tab_control, 'data/web_data/bug_reports.xlsx', 'Vertical.TNotebook')
    checklist_notebook = create_tab_with_sheets(tab_control, 'data/web_data/checklist.xlsx', 'Vertical.TNotebook')

    tab_control.add(test_cases_notebook, text='Тест-кейсы')
    tab_control.add(bug_reports_notebook, text='Баг-репорты')
    tab_control.add(checklist_notebook, text='Чек-лист')

    tab_control.pack(side='left', fill='y')
    return tab_control
