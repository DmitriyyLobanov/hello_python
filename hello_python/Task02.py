# Найти максимальное из пяти чисел

numbers = [2, 3, 5, 1, 8]


def find_max(list_number):
    max = list_number[0]
    for i in list_number:
        if i > max:
            max = i
    return max

print(f'Максимальное число = {find_max(numbers)}.')

