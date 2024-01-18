# Напишите функцию summa_n,
# которая принимает одно целое положительное число N
# и выводит сумму всех чисел от 1 до N включительно.
#
# Пример работы программы:
# Введите число: 5
#
# Я знаю, что сумма чисел от 1 до 5 равна 15
def summa(number):
    numbers_summa = 0
    for summ in range(1, number+1):
        numbers_summa += summ
    print('Сумма чисел: ', numbers_summa)
number = int(input('Введите число: '))
summa(number)