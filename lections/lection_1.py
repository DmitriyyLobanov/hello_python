# Типы данных и переменная
# int, float, boolean, str, list, none.

# value = None
# print(type(value))

# a = 123
# b = 1.23
# value = 1234
# print(value)
# print(type(a))
# print(type(b))

# s = 'Hello World'
# print(a,' - ', b,' - ', s)  # Вывод строк
# print('{} - {} - {}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = True
# print(f)

# list = ['1', '2', '3']
# print(list)

# Ввод и вывод данных
#print('Введите а')
# a = float(input('Введите а:'))
# print('Введите b')
# b = float(input())
# print(a,"+", b,"=", a + b)

# Арифметические операции
# a = 1.3
# b = 3
# c = round(a * b, 3)
# print(c)

# Логические операции
# >, <, >=, <=, ==, !=
# not, and, or - не путать с &, |
# Кое что ещё: is, is not, in, not in

# a = 1 < 4 > 2
# print(a)

# f = [1, 2, 3, 4]
# print(6 in f)

# a = input('a = ')
# b = input('b = ')
# if a > b:
#     print(f'max = {a}')
# else:
#     print(f'max = {b}')

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй хватит.')
# print(inverted)

#list = [1, 2, 3, 4]
# for i in range(5):
#     print(i)


f = [1, 3, 4, 6, 4, 2]
f.append(2)
f.remove(3)
del f[0]
print(f)
