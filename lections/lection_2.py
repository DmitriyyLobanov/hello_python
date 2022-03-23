# colors = ['red', 'green', 'blue', 'add info']
# data = open('lection_2_TXT.txt', 'a')
# # data.writelines(colors)   # Запись в одну строку без разделителей. 
# data.write('LINE2\n')
# data.write('LINE31\n')  
# data.close

# with open('lection_2_TXT.txt', 'w') as data:
#     data.write('line1\n')
#     data.write('line2\n')

# # Чтение с файла:
# path = 'lection_2_TXT.txt'
# data = open('lection_2_TXT.txt', 'r')
# for line in data:
#     print(line)
# data.close()

# def concatenacion(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenacion('a', 's', 'd', 'w')) # asdw
# print(concatenacion('a', '1')) # a1

# # Рекурсия Фибо
# def fib(n):
#     if n in (1, 2): return 1
#     else: return fib(n - 1) + fib(n - 2)

# list = []
# for i in range(1, 10): list.append(fib(i))
# print(list)

# Кортежи
# a = (1, 2)
# print(a)
# print(a[0])

# b = list(a)
# print(b)

# t = ('red', 'green', 'blue')
# red, green, blue = t
# print(f'{red}, {green}, {blue}')

# # Словари
# dictionary = {}
# dictionary = \
#     {
#     'up': 'вверх',
#     'down': 'вниз',
#     'left': 'влево',
#     'right': 'Вправо'
#     }
# # print(dictionary) # {'up': 'вверх', 'down': 'вниз', 'left': 'влево', 'right': 'Вправо'}
# # # print(dictionary['up']) # вверх
# # for k in dictionary.values():
# #     print(k)

# Множества
# colors = {'red', 'green', 'blue'}
# # print(type(colors)) # <class 'set'>
# # print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'gray', 'green', 'blue'}
# colors.remove('red')
# print(colors) # {'gray', 'blue', 'green'}
# # colors,discard('red') # метод который при удалении несуществующего значения не выдаёт ошибку
# colors.clear()
# print(colors) # set()

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # {1, 2, 3, 5, 8}
u = a.union(b) # {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # {8, 2, 5}
dl = a.difference(b) # {1, 3}
dr = b.difference(a) # {13, 21}

q = a \
    .union(b) \
        .difference(a.intersection(b))    # {1, 21, 3, 13}
s = frozenset(a)