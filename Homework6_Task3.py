# Задача 3-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

from functions import give_int_num
print(list(map(lambda i: ((-3)**i), [i for i in range(give_int_num('Введите число: '))])))