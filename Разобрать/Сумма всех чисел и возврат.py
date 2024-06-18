def sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total
print('Сумма чисел:')
print(sum((10, 20, 30, 40, 80)))