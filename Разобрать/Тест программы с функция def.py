import math

# Функция для перевода текста в верхний регистр
def uppercase_text(text):
    return text.upper()

# Функция для расчета длины окружности и площади круга по радиусу
def calculate_circle(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return circumference, area

# Функция для ввода 5 чисел от пользователя
def input_numbers():
    numbers = []
    for i in range(5):
        num = int(input(f"Введите число {i+1}: "))
        numbers.append(num)
    return numbers

# Функция, которая принимает 3 аргумента и возвращает их произведение
def multiply_numbers(a, b, c):
    return a * b * c

# Функция для вывода меню и выбора действия
def menu():
    choice = 0
    while choice != 5:
        print("Меню:")
        print("1. Преобразовать текст в верхний регистр")
        print("2. Расчет длины окружности и площади круга")
        print("3. Ввести 5 чисел")
        print("4. Умножить 3 числа")
        print("5. Выход")

        choice = int(input("Выберите действие: "))

        if choice == 1:
            text = input("Введите текст: ")
            result = uppercase_text(text)
            print("Результат:", result)
        elif choice == 2:
            radius = float(input("Введите радиус: "))
            circumference, area = calculate_circle(radius)
            print("Длина окружности:", circumference)
            print("Площадь круга:", area)
        elif choice == 3:
            numbers = input_numbers()
            print("Введенные числа:", numbers)
        elif choice == 4:
            a = int(input("Введите первое число: "))
            b = int(input("Введите второе число: "))
            c = int(input("Введите третье число: "))
            result = multiply_numbers(a, b, c)
            print("Результат умножения:", result)
        elif choice == 5:
            print("Выход")
        else:
            print("Неверный выбор. Попробуйте еще раз.")

# Вызов функции меню для начала работы программы
menu()