# Напишите функцию count_letters,
# которая принимает на вход текст и подсчитывает,
# какое в нём количество цифр K и букв N.
#
# Функция должна вывести на экран информацию
# о найденных буквах и цифрах в определенном формате.
#
# Пример:
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищём? л
#
# Количество цифр 0: 2
# Количество букв л: 1

def count_letters(text):
    numberCount = 0
    letterCount = 0
    for total in text:
        if total == letter:
            letterCount += 1
        elif total == number:
            numberCount += 1
    print(f'Количество цифр {number}:', numberCount)
    print(f'Количество букв {letter}:', letterCount)

text = input('Введите текст: ')
number = input('Какую цифру ищем? ')
letter = input('Какую букву ищём? ')
count_letters(text)