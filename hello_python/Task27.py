# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

def is_int(str):
    try:
        int(str)
        return True
    except:
        return False


input_string = input('Введите числа через пробел: ').split(' ')
numbers = []
for i in input_string:
    if i.isdigit(): numbers.append(int(i)) 

print(f'Набор чисел: {numbers}.\nНаибольшее число = {max(numbers)}.\nНаименьшее число = {min(numbers)}.')