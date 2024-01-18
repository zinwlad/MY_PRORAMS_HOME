from random import randint
random_value = randint(0, 100)

count = 0

for i in range(1, 11):
    choice = int(input('Введите число: '))
    if choice > random_value:
        print('Много')
    elif choice > random_value:
        print('Мало')
    else:
        print(f'Вы угадали с {i}-й попытки')
        break
    count += 1
    print()
    print(f'Осталось {10-count} попыток')
else:
    print('Вы истратили все попытки, было загадано число', random_valu)
