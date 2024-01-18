# Преобразование веса означает умножение значения единицы на стандартное значение преобразования.
# В этой статье я расскажу вам, как создать графический интерфейс преобразователя веса
# с помощью языка программирования Python.
#
# Стандартные значения преобразования веса включают:
#
# 1 миллиграмм = 0,001 грамм
# 1 сантиграмм = 0,01 грамм
# 1 дециграмм = 0,1 грамм
# 1 килограмм = 1000 граммов
# 1 грамм = 1000 миллиграмм
# 1 тонна = 2000 фунтов
# 1 фунт = 16 унций

from tkinter import *
# Creating a GUI Window
window = Tk()
def from_kg():
    gram = float(e2_value.get())*1000
    pound = float(e2_value.get())*2.20462
    ounce = float(e2_value.get())*35.274
    t1.delete("1.0",END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounce)

e1 = Label(window, text="Input the weight in KG")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e3 = Label(window, text="Gram")
e4 = Label(window, text="Pound")
e5 = Label(window, text="Ounce")

t1 = Text(window, height=5, width=30)
t2 = Text(window, height=5, width=30)
t3 = Text(window, height=5, width=30)

b1 = Button(window, text="Convert", command=from_kg)

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
b1.grid(row=0, column=2)

window.mainloop()