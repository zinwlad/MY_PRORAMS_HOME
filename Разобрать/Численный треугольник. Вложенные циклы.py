'''Дано натуральное число nn. Напишите программу,
которая печатает численный треугольник в соответствии с примером:

1
22
333
4444
55555
...
'''

n = int(input())
for i in range(1, n+1):    # строки n
    for j in range(i):     # столбцы
        print(i, end='')
    print()