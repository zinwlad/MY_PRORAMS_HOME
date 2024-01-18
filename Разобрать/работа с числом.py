inputn = int(input())
n = inputn                        # это наше число, неизменное
total = 0                         # сумма чисел
product = 1                       # произведение чисел
count = 0                         # количество чисел

while inputn != 0:                # цикл пока inputn не равен 0
    total += inputn % 10          # считаем суму чисел
    product *= inputn % 10        # считаем произведение чисел
    count += 1                    # считаем количество чисел
    inputn //= 10                 # откидывает последнее число

print(total)                      # сумма чисел
print(count)                      # количество чисел
print(product)                    # произведение чисел
print(total/count)                # среднее арифмитическое всех чисел
print(n//10 ** (count-1))         # первое число
