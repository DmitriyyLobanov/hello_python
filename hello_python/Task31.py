# Составить список простых множителей натурального числа N

def get_input_int(arg_text):
    """Получение int-ввода пользователем. arg_text - текст приглашение ко вводу."""
    while True:
        try:
            input_value = input(arg_text)
            return int(input_value)
        except:
            print(f'Значение ({input_value}) не является целым числом.')

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

number = get_input_int('Введите целое, положительное число N для разложения на простые множители.\n\
(в случае ввода отрицательного числа, оно автоматически будет взято по модулю):  ')

print(f'Простые множители числа {number} = {prim_factorizacion(number)}.')