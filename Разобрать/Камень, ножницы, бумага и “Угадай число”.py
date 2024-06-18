# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
#
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
#
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
#
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.
import random

def rock_paper_scissors():    #Здесь будет игра "Камень, ножницы, бумага"
    user_action = input("Введите вариант (камень, ножницы, бумага) ")
    possible_actions = ("камень", "бумага", "ножницы")
    computer_action = random.choice(possible_actions)
    print(f"\nВы выбрали {user_action}, компьютер выбрал {computer_action}.\n")

    if user_action == computer_action:
        print(f"Оба игрока выбрали {user_action}. У вас ничья")
    elif user_action == "камень":
        if computer_action == "ножницы":
            print("Камень разбивает ножницы! Ты победил!")
        else:
            print("Бумага покрывает камень! Вы проиграли.")
    elif user_action == "бумага":
        if computer_action == "камень":
            print("Бумага покрывает камень! Ты победил!")
        else:
            print("Ножницы режут бумагу! Вы проиграли.")
    elif user_action == "ножницы":
        if computer_action == "бумага":
            print("Ножницы режут бумагу! Вы выиграли!")
        else:
            print("Камень разбивает ножницы! Вы проиграли.")

def guess_the_number():    #Здесь будет игра "Угадай число"
    from random import randint
    random_value = randint(0, 100)
    count = 0
    for i in range(1, 11):
        choice = int(input('Введите число: '))
        if choice > random_value:
            print('Много')
        elif choice < random_value:
            print('Мало')
        else:
            print(f'Вы угадали с {i}-й попытки')
            break
        count += 1
        print()
        print(f'Осталось {10-count} попыток')
    else:
        print('Вы истратили все попытки, было загадано число', random_value)

def mainMenu():    #Здесь главное меню игры
    print()
    print("В какую игры вы хотите поиграть: \n1 - Камень, ножницы, бумага\n2 - Угадай число\nexit - Выход из игры")
    userMenu = input('Введите номер игры: ')
    if userMenu == '1':
        rock_paper_scissors()
    elif userMenu == '2':
        guess_the_number()
    elif userMenu == 'exit':
        exit()
    else:
        print('Такой игры нет. Введите число')

while True:
    mainMenu()