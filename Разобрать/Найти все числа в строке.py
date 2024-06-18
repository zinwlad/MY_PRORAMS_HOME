index = input('Введите почтовый индекс: ')
index_number = ''
for _ in index:
    if ord('0') <= ord(_) <= ord('9'):
        index_number += _
print(index_number)