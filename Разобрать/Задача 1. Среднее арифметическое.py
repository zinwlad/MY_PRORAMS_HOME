# Задача 1. Среднее арифметическое
# Программа получает от пользователя два числа — a и b. Реализуйте функцию,
# которая принимает на вход числа a и b, считает и выводит в консоль среднее арифметическое
# всех чисел из отрезка [a; b]. Обеспечьте контроль ввода: не забывайте, что а всегда должно быть меньше, чем b.
#
# Усложнение: сделайте это без использования циклов.


def avg_of_range(a, b):
    if a >= b:
        print("Ошибка: левая граница должна быть меньше правой")
        return
    avg = (a + b) / 2
    print("Среднее:", avg)

left_bound = int(input("Введите левую границу: "))
right_bound = int(input("Введите правую границу: "))
avg_of_range(left_bound, right_bound)