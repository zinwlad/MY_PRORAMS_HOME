#Генерация случайных чисел.py
from random import randint
n = int(input())
for i in range(n):
    a = randint(1, 100)
    print(a, end=' ')