# Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека
#     Добавьте игру против бота
#     Подумайте как наделить бота "интеллектом"

import random

def get_input_int(arg_text):
    """Получение int-ввода пользователем. arg_text - текст приглашение ко вводу."""
    while True:
        try:
            input_value = input(arg_text)
            return int(input_value)
        except:
            print(f'Значение ({input_value}) не является целым числом.')
def get_turn(max_turn, turn, remain_candies):
    while (turn > max_turn):
        print('Не превышайте максимальное количество конфет за ход!')
        turn = get_input_int('Сколько конфет возьмете?')
    remain_candies -= turn
    return remain_candies
def get_NPC_turn(max_turn, remain_candies):
    if remain_candies % (max_turn + 1) != 0:
        return remain_candies % (max_turn + 1)
    else:
        return remain_candies / (max_turn + 1)
def rolling_dice():
        tmp = False
        while tmp == False:
            res = [random.randint(1, 6) for i in range(2)]
            if res[0] != res[1]: tmp = True
        return res

# PvP
# candies = get_input_int('Введите количество конфет в игре: ')
# max_turn = get_input_int('Введите количество конфет, доступное для взятия игроком: ')
# player_1 = input('Введите имя первого игрока: ')
# player_2 = input('Введите имя второго игрока: ')

# fate = rolling_dice()
# print(f'Игрок {player_1} выбросил {fate[0]}. Игрок {player_2} выбросил {fate[1]}.')
# if fate[0] > fate[1]:
#     round = 1
#     print(f'Первый ход делает {player_1}.')
# else:
#     round = 2
#     print(f'Первый ход делает {player_2}.')


# round = 1
# while candies > 0:
#     if round == 1:
#         print(f'Очередь игрока - {player_1}, осталось {candies} конфет.')
#         turn = get_input_int('Сколько конфет возьмете? ')
#         candies = get_turn(max_turn, turn, candies)
#         round = 2
#         if candies <= 0: break
#     if round == 2:
#         print(f'Очередь игрока - {player_2}, осталось {candies} конфет.')
#         turn = get_input_int('Сколько конфет возьмете? ')
#         candies = get_turn(max_turn, turn, candies)
#         round = 1
#         if candies <= 0: break

# if round == 2: print(f'Игрок {player_1} победил!')
# elif round == 1: print(f'Игрок {player_2} победил!')


# PvE
candies = get_input_int('Введите количество конфет в игре: ')
max_turn = get_input_int('Введите количество конфет, доступное для взятия игроком: ')
player_1 = input('Введите имя игрока: ')

fate = rolling_dice()
print(f'Игрок {player_1} выбросил {fate[0]}. NPC выбросил {fate[1]}.')
if fate[0] > fate[1]:
    round = 1
    print(f'Первый ход делает {player_1}.')
else:
    round = 2
    print(f'Первый ход делает NPC.')

while candies > 0:
    if round == 1:
        print(f'Очередь игрока - {player_1}, осталось {candies} конфет.')
        turn = get_input_int('Сколько конфет возьмете? ')
        candies = get_turn(max_turn, turn, candies)
        round = 2
        if candies <= 0: break
    if round == 2:
        turn = get_NPC_turn(max_turn, candies)
        print(f'Очередь NPC, NPC взял {turn} конфет.')
        candies -= turn
        round = 1
        if candies <= 0: break

if round == 2: print(f'Игрок {player_1} победил!')
elif round == 1: print(f'NPC победил!')


