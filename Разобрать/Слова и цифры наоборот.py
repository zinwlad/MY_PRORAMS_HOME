prompt = "\nВведите любое слово, и оно будет выведено наоборот"
prompt += "\nЕсли надоело введите команду 'стоп'\n"
active = True
while active:
    message = input(prompt)
    if message == "стоп":
        active = False
        print("Программа завершена")
    else:
        print(message[::-1])