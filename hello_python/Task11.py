#    Сформировать список из  N членов последовательности.
#    Для N = 5: 1, -3, 9, -27, 81 и т.д.

import random

def is_int(str):
    try:
        int(str)
        return True
    except:
        return False

N = input('Введите количество случайных элементов (N): ')

while is_int(N) == False or int(N) <= 0:
   N = input('Неверный ввод, введите количество случайных элементов: ')
else:
    N = int(N)


item = random.randint(-100, 100)
sequence = [item]

for i in range(1, N):
    sequence.append(random.randint(-100, 100))


print(f'Для N = {N}: {sequence}.')
