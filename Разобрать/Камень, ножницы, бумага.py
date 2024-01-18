import random

user_action = input("Введите вариант (камень, ножницы, бумага) ")
possible_actions = ["камень", "бумага", "ножницы"]
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