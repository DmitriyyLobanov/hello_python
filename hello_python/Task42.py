# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах.


data = 'aaaaaacccccssssssrgtggggggttttt'

def rle_encoding(data_str):
    res = ""
    count = 1
    prev_char = ''
    for char in data_str:
        if char != prev_char:
            if prev_char:
                res += f'{str(count)}' + f'{prev_char}'
            count = 1
            prev_char = char
        else:
            count += 1
    return res

print(rle_encoding(data))

def rle_encoding(data_text):
    