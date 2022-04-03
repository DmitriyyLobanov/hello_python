# Дан список чисел. Создать список, в который попадают числа, описывающие возрастающую последовательность.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя.

def create_incr_sequence(numbers):
    res = [numbers[0]]
    for i in numbers:
        if numbers[i] > max(res): res.append(numbers[i])
    return res




numbers = [1, 5, 2, 3, 4, 6, 1, 7]
print(create_incr_sequence(numbers))


