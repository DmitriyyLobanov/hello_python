# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример: k=2 =>   2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def get_input_int(arg_text):
    """Получение int-ввода пользователем. arg_text - текст приглашение ко вводу."""
    while True:
        try:
            input_value = input(arg_text)
            return int(input_value)
        except:
            print(f'Значение ({input_value}) не является целым числом.')
def create_polynom(list_of_elems):
    res = ""
    for i in range(len(list_of_elems)):
        for k in range(len(list_of_elems[i])):
            res += (f'{list_of_elems[i][k]}')
            if k != 1: res += "*x^"
        if list_of_elems[i][k] == 1: res = res[:-2]
        res += " + "
        if i == (len(list_of_elems) - 1): res += (f'{random.randint(0, 101)} = 0')
    return res


degree = get_input_int('Введите старшую степень многочлена: ')
quant_of_elems = degree

elems_of_polynom = []
for i in range(quant_of_elems):
    rand_ratio = random.randint(0, 101)
    elems_of_polynom.append([rand_ratio, degree - i])

polynome_str = create_polynom(elems_of_polynom)

print(elems_of_polynom)
print(polynome_str)

with open('C:hello_python/Task33_Polynome.txt', 'w') as file:
    file.write(polynome_str)

