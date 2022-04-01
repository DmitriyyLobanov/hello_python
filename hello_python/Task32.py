# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
#   Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]   ???



import random

sequence = [random.randint(1, 10) for i in range(10, 20)]
#sequence = [1, 2, 3, 5, 1, 5, 3, 10, 12, 11, 11]

res = list(filter(lambda x: sequence.count(x) == 1, sequence))

print(sequence)
print(res)