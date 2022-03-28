# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19


numbers_list = [1.65, 5, 10.59]


def get_decimal_part(float_number, int_digits_after_point):
    return round((float_number % 1), int_digits_after_point)


dec_part_list = []
for i in range(0, len(numbers_list)):
    if type(numbers_list[i]) == float:
        dec_part_list.append(get_decimal_part(numbers_list[i], 2))


max = max(dec_part_list)
min = min(dec_part_list)

#print(get_decimal_part(numbers_list[5], 2))
print(f'Разница между максимальным и минимальным значением дробной части элемента в списке вещественных чисел:\n{numbers_list} => {max - min}.')
