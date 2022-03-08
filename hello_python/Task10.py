# Найти расстояние между двумя точками пространства

import math


x_1, y_1, z_1 = input('Введите координаты первой точки A(x, y, z) через пробел: ').split()


def is_int(str):
    try:
        int(str)
        return True
    except:
        return False


while is_int(x_1) == False or is_int(y_1) == False or is_int(z_1) == False:
    x_1, y_1, z_1 = input('Неверный ввод, введите координаты первой точки А(x, y, z) через пробел: ').split()
else:
    x_1 = int(x_1)
    y_1 = int(y_1)
    z_1 = int(z_1)

x_2, y_2, z_2 = input('Введите координаты второй точки B(x, y, z) через пробел: ').split()

while is_int(x_2) == False or is_int(y_2) == False or is_int(z_2) == False:
    x_2, y_2, z_2 = input('Неверный ввод, введите координаты второй точки B(x, y, z) через пробел: ').split()
else:
    x_2 = int(x_2)
    y_2 = int(y_2)
    z_2 = int(z_2)

distance = math.sqrt(((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2) + ((z_2 - z_1) ** 2))

print(f'Точка A({x_1}, {y_1}, {z_1}), точка B({x_2}, {y_2}, {z_2})')
print(f'Расстояние между точками: |AB| = {round(distance, 2)}.')
