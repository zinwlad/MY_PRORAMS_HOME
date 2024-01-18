# Вводится последовательность чисел,
# которая оканчивается нулём.
#
# Реализуйте функцию,
# которая принимает в качестве аргумента каждое число,
# переворачивает его и выводит на экран.

def reverse(number):
    reversed_number = 0
    is_negative = number < 0
    if is_negative:
        number = -number
    while number > 0:
        last_digit = number % 10
        reversed_number = reversed_number * 10 + last_digit
        number = number // 10
        if is_negative:
            reversed_number = -reversed_number
    print('Число наоборот:', reversed_number)

number = int(input("Введите число: "))
reverse(number)
