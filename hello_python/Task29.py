# Найти НОК двух чисел  | Наименьшее общее кратное
import math
def get_input_int(arg_text):
    """Получение int-ввода пользователем(С проверкой на положительное число). arg_text - текст приглашение ко вводу."""
    while True:
        try:
            input_value = input(arg_text)
            return abs(int(input_value))
        except:
            print(f'Значение ({input_value}) не является целым числом.')


first_number = get_input_int('Введите первое число: ')
second_number = get_input_int('Введите второе число: ')

def prim_factorizacion(n):
   i = 2
   primfac = []
   while i ** 2 <= n:
       while n % i == 0:
           primfac.append(i)
           n = n / i
       i += 1
   if n > 1:
       primfac.append(n)
   return primfac
def find_SCM (multiples_list_1, multiples_list_2):
    res_list = []
    for i in range(len(multiples_list_2)):
        if multiples_list_1.count(multiples_list_2[i]) == 0:
            res_list.append(multiples_list_2[i])
    res_list.extend(multiples_list_1)
    return math.prod(res_list) 

first_list = prim_factorizacion(first_number)
second_list = prim_factorizacion(second_number)



print(f'Простые множители первого числа {first_number}: {prim_factorizacion(first_number)}.')
print(f'Простые множители второго числа {second_number}: {prim_factorizacion(second_number)}.')
print(f'Наименьшее общее кратное чисел {first_number} и {second_number} = {int(find_SCM(first_list, second_list))}.')


# 1. Разложить оба числа на простые множители.
# 2. Найти множители второго числа, которых нет в списке множителей первого.
# 3. Перемножить множители первого числа на множители второго, не входящие в список множителей первого.
    
