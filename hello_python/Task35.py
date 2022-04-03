# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

import random

def get_input_int(arg_text):
    """Получение int-ввода пользователем. arg_text - текст приглашение ко вводу."""
    while True:
        try:
            input_value = input(arg_text)
            return int(input_value)
        except:
            print(f'Значение ({input_value}) не является целым числом.')

   

N = get_input_int('Введите количество элементов последовательности до вычитания случайного элемента: ')

orignal_sequence = [i for i in range(N)]
del orignal_sequence[random.randint(1, N - 2)]
with open('hello_python/Task35_FILE.txt', 'w') as data:
    for i in orignal_sequence:
        data.write(str(f'{i} '))

with open('hello_python/Task35_FILE.txt', 'r') as data:
    input_sequence = list(map(int, data.read().split()))



test_sequence = [i for i in range(input_sequence[0], len(input_sequence) + 1)]
result = list(set(test_sequence) - set(input_sequence))

print(f'Последовательность, считанная из файла: {input_sequence}.')

print(f'Отсутствующий, отвечающий условию A[i] - 1 = A[i-1] элемент: {result}.')





# for i in orignal_seqence:
#     if orignal_seqence[i] - 1 == orignal_seqence[i-1]: print("ok")
#     else: print("nok")