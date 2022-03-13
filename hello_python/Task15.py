# Написать программу получающую набор произведений чисел от 1 до N.
#  Пример: пусть N = 4, тогда
#   [ 1, 2, 6, 24 ]


import random
N = random.randint(1, 11)

result = []
factorial = 1
for i in range(1, N + 1):
    factorial = factorial * i
    result.append(factorial)

print(f'Для N = {N}: {result}')