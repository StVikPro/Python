# Задача 1- Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день 
# выходным.
# Дополнительно: можете проверить, что это действительно число, 
# и что это действительно входит в нужный диапазон
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

number = int(input("Введите день недели числом от 1 до 7: "))

if number < 1 or number > 7:
    print('Вы ввели неверное число! Проверьте условие!')
elif number > 5:
    print('Ура, выходной!')
else:
    print('Увы, рабочий день - придется поработать!')