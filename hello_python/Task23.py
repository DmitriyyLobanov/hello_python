# Найти произведение пар чисел в списке.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] =>   [12,  15]

numbers = [2, 3, 5, 6] # [2, 3, 4, 5, 6]

def multi_couple(lits_int):
    result = []
    while len(lits_int) > 1:
        result.append(lits_int[0] * lits_int[-1])
        del lits_int[0]
        del lits_int[-1]
        if len(lits_int) == 1: result.append(lits_int[0] ** 2)
    return result

print(multi_couple(numbers))