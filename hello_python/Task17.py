# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число

def is_int(str):
    try:
        int(str)
        return True
    except:
        return False

N = input('Введите N:')
while is_int(N) == False:
    N = input('Неверный ввод, введите N: ')
else:
    N = int(N)

list = [item for item in range(-N, N + 1)]
list_posicion =[]

with open('hello_python/Task17_file.txt', 'r') as file:
   for line in file:
      list_posicion.append(int(line.strip()))
   

product = 1
for i in list_posicion:
    product *= list[i]



print(f'Последовательность элементов: [-N, N]: {list}.')
print(f'Позиции, считанные из файла (Task17_file.txt): {list_posicion}.')
print(f'Произведение элементов на указанных позициях = {product}.')
   
    


