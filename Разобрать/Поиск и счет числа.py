seqNum = int(input('Сколько будем считать? '))
numerall = int(input('Что ищем? '))
while numerall < 0 or numerall > 9:
    numerall = int(input('Введите еще раз что ищем? '))
numeralCount = 0
for num in range(1, seqNum+1):
    print('Введите ', num, 'число ', end='')
    number = int(input())
    while number >0:
        if number % 10 == numerall:
            numeralCount += 1
        number //= 10
print('Цифр', numerall, 'в последовательности', numeralCount)