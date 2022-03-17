# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
#   Примеры
#   список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#   список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
#   список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
#   список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
#   список: [], ищем: "123", ответ: -1


string_list = input('Задайте список строк, символ разделитель - пробел: ').split(' ')
sub_string = input('Введите строку для поиска второго вхождения в списке строк: ')

def find_second_index(str_list, str):
    indexes = []
    if str_list.count(str) < 2: return -1
    else:
        for i in range(0, len(str_list)):
            if str_list[i] == str: indexes.append(i)
            if len(indexes) == 2: return indexes[1]
    


            
print(find_second_index(string_list, sub_string))