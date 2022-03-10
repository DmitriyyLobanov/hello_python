# Подсчитать сумму цифр в вещественном числе.

def is_float(str):
    try:
        float(str)
        return True
    except:
        return False

number = input('Введите вещественное число: ')

while is_float(number) == False:
    number = input('Неверный ввод, ведите вещественное число: ')

if number[0] == '-':
    number = number.replace(".", "")
    number = number.replace("-", "")
else:
    number = number.replace(".", "")

numbers_list = list(number)
numbers_list = [int(item) for item in numbers_list]

print(f'Сумма цифр в вещественном числе = {sum(numbers_list)}.')