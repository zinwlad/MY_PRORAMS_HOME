num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
        flag = False
        break

if flag:
    print('Число простое')
else:
    print('Число составное')