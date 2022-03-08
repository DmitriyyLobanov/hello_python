# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sanday']
number_of_day = input('Введите число: ')

def is_int(str):
    try:
        int(str)
        return True
    except:
        return False

while is_int(number_of_day) == False:
    number_of_day = input('Неверный ввод, ведите число: ')
else:
    number_of_day = int(number_of_day)

if 0 < number_of_day < 8:
    if number_of_day <= 5:
        print(f'{week[number_of_day - 1]} - будний день.')
    else:
        print(f'{week[number_of_day - 1]} - выходной день.')
else:
    print('Введено число не имеющее соответствия с днем недели.')
