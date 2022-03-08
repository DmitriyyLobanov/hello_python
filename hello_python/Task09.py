# Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти


quarter = input('Введите номер четверти прямоугольной системы координат: ')

def is_int(str):
    try:
        int(str)
        return True
    except:
        return False

while is_int(quarter) == False or int(quarter) < 1 or int(quarter) > 4:
    quarter = input('Некорректный ввод, введите номер четверти прямоугольной системы координат: ')
else:
    quarter = int(quarter)

if quarter == 1: print('Первой четверти прямоугольной системы координат соответствуют координаты (x > 0, y > 0).')
elif quarter == 2: print('Второй четверти прямоугольной системы координат соответствуют координаты (x < 0, y > 0).')
elif quarter == 3: print('Третьей четверти прямоугольной системы координат соответствуют координаты (x < 0, y < 0).')
elif quarter == 4: print('Четвертой четверти прямоугольной системы координат соответствуют координаты (x > 0, y < 0).')

