# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]



numbers = [1, 2, 3, 5, 1, 5, 3, 10]
unic_numbers = list(filter(lambda x: numbers.count(x) == 1, numbers))

print(f'{numbers} => {unic_numbers}')
