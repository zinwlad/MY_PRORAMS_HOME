# Чтобы создать игру-угадайку, нам нужно написать программу для выбора случайного числа
# от 1 до 10. Чтобы дать пользователю подсказки, мы можем использовать условные операторы ,
# чтобы сообщить пользователю, является ли угаданное число меньше, больше или равно случайно выбранное число.
#
# Итак, ниже показано, как вы можете написать программу для создания игры с угадыванием чисел с помощью Python:

import random
n = random.randrange(1,10)
guess = int(input("Enter any number: "))
while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else: