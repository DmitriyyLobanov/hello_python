# Написать программу преобразования десятичного числа в двоичное

def is_int(str):
    try:
        int(str)
        return True
    except:
        return False

number = input('Введите десятичное число: ')
while is_int(number) == False:
    number = input('Некорректный ввод, введите десятичное число: ')
else: number = int(number)


print(f'{number} => {bin(number)}')