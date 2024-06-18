people = int(input('Введите кол-во людей: '))
for hour in range(people +1):
    print('Идет час: ', hour)
    for num in range(hour, people):
        print('Номер в очереди: ', num)
    print()
print('Все люди в очереди обслужены!')