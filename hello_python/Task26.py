# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
# Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

def get_input_int(arg_text):
    """Получение int-ввода пользователем. arg_text - текст приглашение ко вводу."""
    while True:
        try:
            input_value = input(arg_text)
            return int(input_value)
        except:
            print(f'Значение ({input_value}) не является целым числом.')



number = get_input_int("Введите k: ")

def fibo_rec(number_int):
    if number_int in (1, 2):
        return 1
    return fibo_rec(number_int - 1) + fibo_rec(number_int - 2)

def negafibo(number_int):
    fib1 = fib2 = 1
    for i in range(-number_int, 1):
        fib1, fib2 = fib2, fib1 - fib2
    return fib2

fibo_list =[fibo_rec(item) for item in range(number, 0, -1)]
fibo_list.reverse()

negafibo_list = [negafibo(item) for item in range(number + 1)]
negafibo_list.reverse()

negafibo_list.extend(fibo_list)
print(f'Для k = {number} список примет вид: {negafibo_list}.')

