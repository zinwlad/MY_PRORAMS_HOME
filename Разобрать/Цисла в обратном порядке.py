n = int(input('Введите число '))
s = 0
while n > 0:
    b = n % 10
    s = s * 10 + b
    n = n // 10
print(s)