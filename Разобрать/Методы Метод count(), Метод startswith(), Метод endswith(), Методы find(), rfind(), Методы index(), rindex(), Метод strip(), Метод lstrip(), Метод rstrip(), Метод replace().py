text = "   Hi, World! Hello, Python   "

# count - подсчитывает количество вхождений подстроки в строке
print(f"Количество вхождений 'Hello': {text.count('Hello')}")

# startswith - проверяет, начинается ли строка с указанной подстроки
if text.startswith("Hello"):
    print("Строка начинается с 'Hello'")

# endswith - проверяет, заканчивается ли строка указанной подстрокой
if text.endswith("Python!"):
    print("Строка заканчивается на 'Python!'")

# find - ищет первое вхождение указанной подстроки в строке и возвращает индекс (или -1, если подстрока не найдена)
index = text.find("Python")
if index != -1:
    print(f"Первое вхождение 'Python' на позиции {index}")

# rfind - ищет последнее вхождение указанной подстроки в строке и возвращает индекс (или -1, если подстрока не найдена)
index = text.rfind("Hello")
if index != -1:
    print(f"Последнее вхождение 'Hello' на позиции {index}")

# index - аналогично методу find, но вызывает исключение ValueError, если подстрока не найдена
try:
    index = text.index("world")
    print(f"Первое вхождение 'world' на позиции {index}")
except ValueError:
    print("Подстрока 'world' не найдена")

# rindex - аналогично методу rfind, но вызывает исключение ValueError, если подстрока не найдена
try:
    index = text.rindex("Hello")
    print(f"Последнее вхождение 'Hello' на позиции {index}")
except ValueError:
    print("Подстрока 'Hello' не найдена")

# strip - удаляет пробельные символы в начале и конце строки
text = text.strip()
print(f"Строка без пробельных символов: '{text}'")

# lstrip - удаляет пробельные символы в начале строки
text = "  " + text.lstrip()
print(f"Строка без пробельных символов в начале: '{text}'")

# rstrip - удаляет пробельные символы в конце строки
text = text.rstrip() + "  "
print(f"Строка без пробельных символов в конце: '{text}'")

# replace - заменяет указанную подстроку другой подстрокой в строке
new_text = text.replace("Hello", "Hi")
print(f"Новая строка после замены: '{new_text}'")