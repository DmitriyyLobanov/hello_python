#    Сформировать список из  N членов последовательности.
#    Для N = 5: 1, -3, 9, -27, 81 и т.д.

import random

def is_int(str):
    try:
        int(str)
        return True
    except:
        return False

N = input('Введите количество элементов (N): ')

while is_int(N) == False or int(N) <= 0:
   N = input('Неверный ввод, введите количество случайных элементов: ')
else:
    N = int(N)

item = 1
sequence = [item]

for i in range(1, N):
    item *= 3
    sequence.append(item)

for i in range(0, N):
    if i % 2 != 0: sequence[i] *= -1


print(f'Для N = {N}: {sequence}.')
