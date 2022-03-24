# Найти корни квадратного уравнения Ax² + Bx + C = 0
#     Математикой
#     Используя дополнительные библиотеки*


from math import sqrt

A = 1
B = -11
C = 18

def find_discriminate(vol_A, vol_B, vol_C):
    return pow(vol_B, 2) - 4 * vol_A * vol_C

D = find_discriminate(A, B, C)
if D < 0: 
    print('Отрицательный дискриминант, уравнение не имеет действиетльных корней!')
    exit()


x_1 = (-B + (sqrt(D))) / (A * 2)
x_2 = (-B - (sqrt(D))) / (A * 2)

print(find_discriminate(A, B, C))
print(x_1, x_2)