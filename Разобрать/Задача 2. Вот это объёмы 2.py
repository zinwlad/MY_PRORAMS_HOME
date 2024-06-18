# Задача 2. Вот это объёмы 2


# Напишите программу, которая на вход получает от пользователя радиус планеты (вещественное число) и вызывает функции
# sphereArea и sphereVolume. Реализуйте эти функции: первая считает и выводит на экран площадь сферы, вторая — объём шара.
#
#
#

def sphere_area(radius):
    print(4 * math.pi * radius ** 2)


def sphere_volume(radius):
    print(4 / 3 * math.pi * radius ** 3)


radius_of_planet = float(input("Введите радиус планеты: "))
sphere_area(radius_of_planet)
sphere_volume(radius_of_planet)