name = input('Введите ваше имя: ')
debt = int(input('Какая ваша задолженость? '))
print('Ваша задолжность состовляет: ', debt)
payment = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? '))
while payment < debt:
    print('Маловато, ', name+, '. Давайте ещё раз.')
    transactions = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? '))
    break
print('Отлично, ', name+, '! Вы погасили долг. Спасибо!')

