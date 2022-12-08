# Задача 5- Напишите программу, которая принимает на вход 
# координаты двух точек и находит расстояние между ними в 2D 
# пространстве.
# Пример:
# A (3,6); B (2,1) -> 5.09
# A (7,-5); B (1,-1) -> 7.21

x1 = int(input('Введите координаты х1: '))
y1 = int(input('Введите координаты y1: '))
x2 = int(input('Введите координаты х2: '))
y2 = int(input('Введите координаты y2: '))
import math
sqrt = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2),2)
print(f'Расстояние: (от A - ({x1}, {y1}) до B - ({x2}, {y2}) = {sqrt}')