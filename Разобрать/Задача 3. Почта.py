def myAdress():
    print('Фамилия: Иванов')
    print('Имя: Василий')
    print('Улица: Пушкина')
    print('Дом: 32')
    print()

myAdress()
myAdress()
myAdress()

# Вариант посложнее, с забеганием вперед:

# def print_all_info(surname, name, street, house):
#     print(f"Фамилия: {surname}\n"
#           f"Имя: {name}\n"
#           f"Улица: {street}\n"
#           f"Дом: {house}")
#
#
# user_surname = input("Введите фамилию: ")
# user_name = input("Введите имя: ")
# user_street = input("Введите улицу: ")
# user_house = input("Введите номер дома: ")
#
# for _ in range(3):
#     print_all_info(user_surname, user_name, user_street, user_house)