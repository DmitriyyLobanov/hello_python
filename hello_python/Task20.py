# Определить, присутствует ли в заданном списке строк, некоторое число 

def is_int(str):
    try:
        int(str)
        return True
    except:
        return False

def find_int(str_list, some_int):
    result = False
    for i in range(0, len(str_list)):
        if string_list[i] == str(some_int): result = True
    return result



string_list = input('Задайте список строк, символ разделитель - пробел: ').split(' ')
some_number = input('Введите число для поиска в списке строк: ')

while is_int(some_number) == False:
    some_number = input('Неверный ввод, введите число для поиска в списке строк: ')
else: some_number = int(some_number)

if find_int(string_list, some_number) == True: print(f'Число {some_number} присутствует в списке строк: {string_list}.')
else: print(f'Число {some_number} не присутствует в списке строк: {string_list}.')


