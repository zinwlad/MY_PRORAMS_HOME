def multiply(numbers):
    total = 0
    for n in numbers:
        total += n
    return total
print('Уножение чисел:')
print(multiply((10, 20, 30, 40, 80)))