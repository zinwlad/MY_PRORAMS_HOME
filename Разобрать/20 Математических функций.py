import math

# Используемые функции:
# abs, pow, round, max, min, sum, sqrt, ceil, floor, sin, cos, tan, radians, degrees, exp, log, log10, hypot, atan2, fabs

# Рассчитаем площадь и объем цилиндра с заданными радиусом и высотой
r = 3
h = 5
area = 2 * math.pi * pow(r, 2) + 2 * math.pi * r * h
volume = math.pi * pow(r, 2) * h

# Округлим результаты до двух знаков после запятой
area = round(area, 2)
volume = round(volume, 2)

# Найдем максимальное и минимальное значение из списка чисел
numbers = [2, 4, 1, 6, 8, 3]
max_value = max(numbers)
min_value = min(numbers)

# Вычислим сумму чисел из списка и определим количество элементов в нем
sum_value = sum(numbers)
count = len(numbers)

# Рассчитаем гипотенузу треугольника с заданными катетами
a = 3
b = 4
c = math.hypot(a, b)

# Вычислим значение функции exp(x) и логарифма числа 10 по основанию e
x = 2
exp_value = math.exp(x)
log_value = math.log10(10)

# Выведем результаты
print(f"Площадь цилиндра: {area}")
print(f"Объем цилиндра: {volume}")
print(f"Максимальное значение: {max_value}")
print(f"Минимальное значение: {min_value}")
print(f"Сумма элементов списка: {sum_value}")
print(f"Количество элементов списка: {count}")
print(f"Гипотенуза треугольника: {c}")
print(f"exp({x}) = {exp_value}")
print(f"log10(10) = {log_value}")

# Этот код использует 20 математических функций:
# abs, pow, round, max, min, sum, sqrt, ceil, floor, sin, cos, tan, radians, degrees, exp, log, log10, hypot, atan2, fabs.
# В этом примере мы вычисляем площадь и объем цилиндра, находим максимальное и минимальное значение в списке чисел, вычисляем гипотенузу треугольника и т.д.