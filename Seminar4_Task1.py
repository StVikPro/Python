# Задача 1. Задайте строку из набора чисел. Напишите программу, 
# которая покажет большее и меньшее число. В качестве 
# символа-разделителя используйте пробел.

str_nums = input('Введите числа через пробел: ').split(' ') #ввели 2 числа
nums = [] # получили массив со стринговыми переменными
for i in str_nums:
    nums.append(int(i)) # превратили в массив с числами
print(f'max - {max(nums)}, mix - {min(nums)}') # вывели на печать
