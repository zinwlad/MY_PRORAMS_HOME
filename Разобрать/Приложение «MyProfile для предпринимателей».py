# MyProfile app

SEPARATOR = '------------------------------------------'

# Пользователь
name = ''
age = 0
phone = ''
email = ''
index = 0
adress = ''
info = ''
# Банковские реквизиты
OGRNIP = 0
INN = 0
checking_account = 0
bank_name = ''
BIC = 0
correspondent_account = 0


def general_info_user(name_parameter, age_parameter, phone_parameter, email_parameter, index_parameter, adress_parameter, info_parameter):
    print(SEPARATOR)
    print('Имя:    ', name_parameter)

    if 11 <= age_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif age_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'
    print('Возраст: ', age_parameter, years_parameter)
    print('Телефон: ', phone_parameter)
    print('E-mail: ', email_parameter)
    print('Индекс: ', index_parameter, )
    print('Адрес: ', adress_parameter)
    if info:
        print('')
        print('Дополнительная информация:')
        print(info_parameter)
    return name_parameter, phone_parameter, email_parameter, index_parameter, adress_parameter, info_parameter


def general_info_bank(OGRNIP_parameter, INN_parameter, checking_account, bank_name_parameter, BIC_parameter, correspondent_account_parameter):
    print('Информация о предпринимателе')
    print('ОГРНИП:', OGRNIP_parameter)
    print('ИНН:', INN_parameter)
    print('Расчётный счёт:', checking_account)
    print('Название банка: ', bank_name_parameter)
    print('БИК: ', BIC_parameter)
    print('Корреспондентский счёт: ', correspondent_account_parameter)



print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # Введите общую информацию
                name = input('Введите имя: ')
                while 1:
                    # validate user age
                    age = int(input('Введите возраст: '))
                    if age > 0 and age < 101:
                        break
                    print('Не верный возраст')

                uph = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone = ''
                for ch in uph:
                    if ch == '+' or ('0' <= ch <= '9'):
                        phone += ch

                email = input('Введите адрес электронной почты: ')

                index = input('Введите почтовый индекс: ')
                digits = [c for c in index if c.isdigit()]
                index = ''.join(digits)

                adress = input('Введите почтовый адрес (без индекса): ')
                info = input('Введите дополнительную информацию:\n')

            elif option2 == 2:

                # банк
                OGRNIP = input('Введите ОГРНИП: ')
                while len(OGRNIP) != 15:
                    print('ОГРНИП должен содержать 15 цифр')
                    OGRNIP = input('Введите ОГРНИП: ')
                OGRNIP = int(OGRNIP)

                INN = int(input('ИНН: '))
                checking_account = input('Введите расчётный счёт: ')
                while len(checking_account) != 20:
                    print('Расчетный счет должен содержать 20 цифр. Введите еще раз.')
                    checking_account = input('Введите расчётный счёт: ')
                checking_account = int(checking_account)
                bank_name = input('Введите название банка: ')
                BIC = input('Введите БИК: ')
                correspondent_account = input('Введите корреспондентский счёт: ')

            else: print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(name, age, phone, email, index, adress, info)
            elif option2 == 2:
                general_info_user(name, age, phone, email, index, adress, info)
                print('')
                general_info_bank(OGRNIP, INN, checking_account, bank_name, BIC, correspondent_account)
            else:
                print('Введите корректный пункт меню')