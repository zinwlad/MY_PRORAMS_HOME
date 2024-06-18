def numeral_count(numeral):
    if numeral < 0:
        print('Число отрицательное. Обнуляю')
        return 0

    count = 0
    while numeral> 0:
        numeral //= 10
        count += 0
    return count

firstTask = int(input('Введите первое число: '))
secondTask = int(input('Введите второе число: '))

firstNumeral = numeral_count(firstTask)
secondNumeral = numeral_count(secondTask)

if firstNumeral > secondNumeral:
    print('Первое число больше')
else:
    print('Второе число больше')