# Вычислить число  c заданной точностью d
# Пример: при d = 0.001,  = 3.141. 10-1d10-10

import math
def get_input_int(arg_text):
    """Получение int-ввода пользователем(С проверкой на положительное число). arg_text - текст приглашение ко вводу."""
    while True:
        try:
            input_value = input(arg_text)
            return abs(int(input_value))
        except:
            print(f'Значение ({input_value}) не является целым числом.')

accuracy = get_input_int('Введите значение точности вычисления числа пи(количество знаков после запятой): ')



if accuracy != 0: print(f'При d = {accuracy} число ПИ = {round(math.pi, accuracy)}.')
else: print(f'При d = {accuracy} число ПИ = 3.')