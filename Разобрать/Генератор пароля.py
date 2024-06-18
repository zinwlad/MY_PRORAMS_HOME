import random

alhabet = 'qwertyuiopasdfghjklzxcvbnm'
digits = '0123456789'
password = ''
s = alhabet + digits + digits
for n in range(10):
    password += random.choice(s)
print(password)




