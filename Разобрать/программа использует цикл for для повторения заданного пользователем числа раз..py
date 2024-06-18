'''
Эта программа использует цикл for для повторения заданного пользователем числа раз.
На каждой итерации программа предлагает пользователю ввести целое число, которое хранится
в переменной «элемент». Затем программа проверяет, использует ли «элемент» оператор if.
Если элемент четный, программа увеличивает переменную «count» и добавляет элемент к «total».
В конце цикла программа выводит количество четных элементов и общее количество четных элементов.'''

count = 0
total = 0

# Prompt user for input
num_elements = int(input("Enter the number of elements: "))

# Loop through and get input from the user
for i in range(num_elements):
    element = int(input("Enter element #" + str(i+1) + ": "))
    if element % 2 == 0:
        count += 1
        total += element

# Print results
print("Number of even elements:", count)
print("Total of even elements:", total)