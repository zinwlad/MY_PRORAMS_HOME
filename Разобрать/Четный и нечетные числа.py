number = int(input('Введите число'))
k1 = 0
k2 = 0
while number > 0:
    b = number % 10
    if b % 2 == 0:
        k1 += 1
    else:
        k2 += 1
    number //= 10
print(k1, k2)