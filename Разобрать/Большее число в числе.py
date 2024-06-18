n = int(input())
mx = -1000
while n > 0:
    b = n % 10
    if b > mx:
        mx = b
    n = n // 10
print(mx)

