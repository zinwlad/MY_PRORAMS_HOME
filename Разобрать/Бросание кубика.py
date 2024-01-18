import random

score1 = 0
score2 = 0
die1 = 0
die2 = 0

input('Первый игрок бросает кубик, нажмите Enter!\n')

while score1 < 5 and score2 < 5:

    die1 = random.randint(1, 6)
    print(die1,'\n')
    input('Теперь бросает кубик второй игрок, нажмите Enter!\n')

    die2 = random.randint(1, 6)
    print(die2,'\n')

    if die1 > die2:
        score1 += 1
    elif die1 < die2:
        score2 += 1
    else:
        print('Ничья\n')
    print('Счёт', score1, ':', score2,'\n')
    input('Нажмите Enter!\n')

if score1 > score2:
    input('Победил первый игрок! Нажмите Enter для выхода')
else:
    input('Победил второй игрок! Нажмите Enter для выхода')