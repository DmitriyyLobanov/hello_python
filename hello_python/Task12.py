#    Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
#    Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


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

dict = {}

for i in range(1, N + 1):
    dict.update ({i: 3 * N + 1})

print(f'Для N = {N}: {dict}')
