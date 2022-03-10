# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

first_string = input('Введите строку: ')
second_string = input('Введите подстроку: ')

print(f'Строка: ({first_string}).\nПодстрока: ({second_string}).\nКоличество вхождений подстроки в строку = {first_string.count(second_string)}.')

