#Задача 3- Напишите программу, которая будет на вход принимать 
# число N и выводить числа от -N до N

# *Примеры:* 

# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

number = int(input('Введите число:\n')) #просим на вход число и взять число по модулю
opposite_number = -number #делаем отрицательное число
if number > opposite_number:
    new_range = list(range(opposite_number, number + 1))#делаем диапазон от отрицательного до N и с помощью функии list делаем список
else:
    new_range = list(range(number, opposite_number + 1))#делаем диапазон от N положительного и с помощью функии list делаем список
print(new_range)
