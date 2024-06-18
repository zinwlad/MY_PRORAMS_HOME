interview = {}
active = True
while active:
    # Запрашиваем имя и ответ на вопрос
    name = input("\nКак вас зовут? ")
    question = input("Какая марка автомобиля вам нравиться ")
    # Создаем список с ответами и добавляем первый ответ
    answers = []
    answers.append(question)
    # Ответ сохраняем в словаре "имя: список ответов"
    interview[name] = answers

    # Запускаем второй цикл с возможностью добавления еще ответов к одному пользователю
    active_2 = True
    while active_2:
        repeat = input("Желаете добавить еще один автомобиль? (yes/no)  ")
        if repeat == 'no':
            active_2 = False
        else:
            question_n = input("Какая марка автомобиля вам еще нравиться ")
            # Добавляем ответ в список
            answers.append(question_n)

    # Вопрос о продолжение опроса
    repeat = input("Желаете продолжить опрос? (yes/no) ")
    if repeat == 'no':
        active = False
print("\nОпрос завершен, все результаты:")


# Переберем словарь и посмотрим ответы
for name, questions in interview.items():
    print(f"\n{name.title()} любит автомобили марки:")
    for question in questions:
        print(f"\t{question.title()}")