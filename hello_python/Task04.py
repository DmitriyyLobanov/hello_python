# Показать первую цифру дробной части числа

float_number = input('Введите дробное число: ')

def is_float(str):
    try:
        float(str)
        return True
    except:
        return False

while is_float(float_number) == False:
    float_number = input('Неверный ввод, ведите число: ')

float_number = float(float_number)
result = int((float_number * 10 ) % 10)
print(f'Первая цифра дробной части числа {float_number} = {result}')

