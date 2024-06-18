import random

goal1 = 0
goal2 = 0
time = 1

while goal1 == 0 and goal2 == 0:
    attack = random.randint(1, 2)
    if attack == 1:
        shoot = random.randint(1, 2)
        if shoot == 1:
            keeper = random.randint(1, 2)
            if keeper == 1:
                print('Шайба отбита вратарём ЦСКА, матч продолжается')
                time += 1
                attack = random.randint(1, 2)
            else:
                print('Гооол! СКА побеждает 1:0!')
                goal1 += 1
        else:
            print('Нападающий СКА пробил мимо ворот')
            time += 1
            attack = random.randint(1, 2)
    else:
        shoot = random.randint(1, 2)
        if shoot == 1:
            keeper = random.randint(1, 2)
            if keeper == 1:
                print('Шайба отбита вратарём СКА, матч продолжается')
                time += 1
                attack = random.randint(1, 2)
            else:
                print('Гооол! ЦСКА побеждает 0:1!')
                goal2 += 1
        else:
            print('Нападающий ЦСКА пробил мимо ворот')
            time += 1
            attack = random.randint(1, 2)

print('Матч окончен на', time, 'минуте дополнительного времени.')
input()