# Реализовать алгоритм перемешивания списка. 


from random import randrange

def sattolo_cycle(items):
    i = len(items)
    while i > 1:
        i = i - 1
        j = randrange(i)  # 0 <= j <= i-1
        items[j], items[i] = items[i], items[j]
    return items


list = [1, 2, 3, 4, 5]
print(f'Начальный список: {list}.')
print(f'Перемешанный список: {sattolo_cycle(list)}.')

