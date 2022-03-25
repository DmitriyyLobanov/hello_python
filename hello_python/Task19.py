# Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел

from random import shuffle
import time

def stupid_accident(start, stop):
    """Генератор псевдослучайных чисел: (начало диапазона, конец диапазона)"""
    sequence = [items for items in range(start, stop + 1)]
    seconds = str(time.time())
    index = int(seconds[len(seconds) - (len(str(stop)) - 1): ])
    shuffle(sequence)
    return sequence[index]
    

print(stupid_accident(1, 10))

test_distribution = [stupid_accident(0, 10) for i in range(10000)]
for i in range(11):
    print(f'{i}: {test_distribution.count(i)}')
    

# print(test_distribution)