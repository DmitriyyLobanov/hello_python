# Пример передачи функции как аргумента другой функции
# def sum(x, y):
#     return x + y

# def mult(x, y):
#     return x * y

# def calc(op, a, b):
#     return op(a, b)

# print(calc(lambda x, y: x + y, 5, 5))


# Пример list comprehension
# list = []

# for i in range(1, 101):
#     if i % 2 == 0:
#         list.append(i)

# import math


# # list = [(i, math.pow(i, 3)) for i in range(1, 21) if i % 2 == 0]
# print(list)

# Пример map()

# li = [i for i in range(1, 20)]
# li = list(map(lambda x: x + 10, li))
# print(li)

# data = list(map(int ,input().split()))
# print(data)

# Пример filter()
# li = [i for i in range(1, 11)]
# res = list(filter(lambda x: not x % 2, li))
# print(res)

# Пример zip()
users = ['user1', 'user2', 'user3', 'user4', 'user5']
# id = [4, 2, 3, 5, 7]
# salary = [111, 222, 333]

# data = list(zip(users, id, salary))
# print(data)

# Пример enumerate()
data = list(enumerate(users))
print(data)