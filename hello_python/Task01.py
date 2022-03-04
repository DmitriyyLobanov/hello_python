# По двум заданным числам проверить является ли одно квадратом второго

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))

def square_check(checked_number, exponentiated_number):
    if exponentiated_number ** 2 == checked_number:
        return True
    else:
        return False

if square_check(second_number, first_number) == True:
    print(f'Число {second_number} явялется квадратом числа {first_number}.')
else:
    print(f'Число {second_number} не явялется квадратом числа {first_number}.')

if square_check(first_number, second_number) == True:
    print(f'Число {first_number} явялется квадратом числа {second_number}.')
else:
    print(f'Число {first_number} не явялется квадратом числа {second_number}.')