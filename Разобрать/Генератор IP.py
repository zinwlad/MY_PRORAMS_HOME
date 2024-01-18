number = int(input())
step = int(input())
sum = 0
print('\nIP-адрес: ', end = '')
for count in range(3):
    print(number, end='.')
    sum += number
    number += step
print(sum)