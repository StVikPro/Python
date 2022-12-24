# Задача 2 Задайте два числа. Напишите программу, которая найдет 
# НОК (наименьшее общее кратное) этих двух чисел. 
# НОК - наименьшее общее кратное, которое делится и на первое, 
# и на второе число.

def nod(num1, num2): # функция поиска наименьшего общего делителя
    if not num1 % num2:
        nod = num2
        return nod
    else:
        while num2 > 0 or num1 > 0:
            temp = num1
            num1 = num2
            num2 = temp % num2
            if not num1 % num2:
                nod = num2
                return nod
nums = input('Введите два числа через пробел: ').split(' ') # ввели два числа
num1 = int(nums[0]) # получили из списка два элемента
num2 = int(nums[1]) # получили из списка два элемента

nod_num = nod(num1, num2)
nok = int(num1*num2/nod_num) # наибольшее общее кратное
print(f'НОК для {num1} и {num2} -> {nok}')