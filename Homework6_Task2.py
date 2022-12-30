# Задача 2- Найти произведение пар чисел в списке. Парой считаем 
# первый и последний элемент, второй и предпоследний и т.д.

from random import randint


number = int(input('Введите размер Вашего списка '))
list = []
list2 = []

for i in range(number):
    list.append(randint(0, 9))

for i in range(len(list)):
    while i < len(list)/2 and number > len(list)/2:
        number = number - 1
        a = list[i] * list[number]
        list2.append(a)
        i += 1

print(f'Введенный список {list}')
print(f'Произведение пар чисел в списке {list2}')