# Задача 1 - Напишите программу, которая принимает на вход вещественное 
# число и показывает сумму его цифр. Учтите, что числа могут быть 
# отрицательными
# Пример:
# 67.82 -> 23
# (-0.56) -> 11

num = input('Введите число: ')# input сразу вностит строку str
sum = 0
for i in num:
    if i.isdigit():# проверяем является ли каждый символ числом
        sum += int(i)#если является числом после сложения конвертируем в целове значение
print(sum)