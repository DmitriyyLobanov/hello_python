# Вывести на экран числа от -N до N


number = input('Введите число: ')

def is_int(str):
    try:
        int(str)
        return True
    except:
        return False

while is_int(number) == False:
    number = input('Неверный ввод, ведите число: ')

for i in range(-int(number), int(number) + 1):
    print(i)

