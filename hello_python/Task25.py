# Написать программу преобразования десятичного числа в двоичное

# def get_input_int(arg_text):
#     """Получение int-ввода пользователем. arg_text - текст приглашение ко вводу."""
#     while True:
#         try:
#             input_value = input(arg_text)
#             return int(input_value)
#         except:
#             print(f'Значение ({input_value}) не является целым числом.')
   

# number = get_input_int('Введите десятичное число: ')

# print(f'{number} => {bin(number)}')


def hex_to_decim (hex_str):
    letters_dict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    res = 0
    count = 0
    for char in reversed(hex_str):
        if char in letters_dict.keys():
            char = letters_dict.get(char)
        else: char = int(char)
        res += char * pow(16, count)
        count += 1
    return res






# letters_dict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
print(hex_to_decim("C921"))