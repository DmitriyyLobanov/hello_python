# Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

number = input('Введите число: ')

def is_int(str):
    try:
        int(str)
        return True
    except:
        return False

while is_int(number) == False:
    number = input('Неверный ввод, ведите число: ')
else:
    number = int(number)

if number % 5 == 0 and number % 10 == 0:
    print(f'Число {number} кратно 5 и 10.')
elif number % 15 == 0 and number % 30 != 0:
    print(f'Число {number} кратно 15 но не 30.')
else:
    print(f'Число {number} не удовлетворяет ни одному из условий.')


