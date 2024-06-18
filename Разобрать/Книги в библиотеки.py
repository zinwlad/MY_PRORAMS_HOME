books_id = [58, 40, -1, 9, -1, 87]
new_books_id = []
returned = 0

for _ in range(10):
    id = int(input('Введите ID книги: '))
    books_id.append(id)
for id in books_id:
    if id == -1:
        returned += 1
    else:
        new_books_id.append(id)

print('Новый список выданных книг', new_books_id)
print('Количество вернувших книг', returned)