# Задача 2 Для натурального(целочисленного) N создать словарь
# индекс значение для элементов последовательности 3N + 1
# Длля 6 например, где ключ это значение от 1 до 6 а значение 
# 3*1 + 1 3*2 + 1 и т.д.
num = int(input('Введите значение: '))
dct = {}
for i in range(1, num + 1):
    dct[i] = 3*i + 1
print(dct)

# сокращенный вариант
# dct = {i: 3*i +1 for i in range(1, int(input()) + 1)} 
# print(dct)