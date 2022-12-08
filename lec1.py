##print ('Hello world')


value = None # None присваевается value так как просто так ее
# записать нельзя, только через None
a = 123
b = 1.23
print (a)
print (b)
#value = 12345
#print (value)


#print (type(a)) ##type -  чтобы увидеть тип переменной
#print (type(b))
#value = 12345
#print (type(value))


s = 'hello world' #s - это указываем опертор строки
print (s) # вывод строки

s = "hello 'world" # '' или "" если хотим апостроф или ковычки поставить внутри
print (s) # вывод строки

# Интерполяция как вывести несколько переменных через print

print(a, b, s) # вывод нескольких переменных
print(a, '-',b, '-',s) # вывод строк между результатами
print('{} - {} - {}'.format(a, b, s)) #форматированный вывод описав шаблон
print(f'{a} - {b} - {s}')#вывод с интерполяцией впереди добавив f
print('{0} - {2} - {1}'.format(a, b, s))#вывод с изменением порядка значения переменных согласно ИНДЕКСА переменных

f = True #True или False логические переменные
print(f)

#Списки заменяют массивы в Python

list = [1, 2, 3] #обьявление чего то похожего на массив
print(list)#вывод массива
list = ['1', '2', '3', 'hello world']# вывод текста
print(list)
col = ['1', '2', '3', 'hello world', 1, 1.23]
print(col)

#Ввод и вывод данных. Преобразование типов
##print('Введите a');
#a = input()
#a = int(input()) #чтобы получить при сумме целочисленное число а не строку
##a = float(input())# чтобы получить вещественные с запятой
##print('Введите b');
#b = input()
#b = int(input())
##b = float(input())
##print(a, b)
##print('{} {}'.format(a, b))
##print(f'{a} {b}')
##print(a, ' ', b, ' ', a+b)# благодаря int получаем число а не строки

# Арифметические операции

a = 1.3
b = 3
c = a + b 
#a*b умножение
#a/b деление
#a//b деление в целых числах
#a%b получить остаток от делания
#a**b возведение в степень
#round(a*b, 3) round - это окрузление, а 3 значение цифр округления

#a=3
#a=a+ 5 равносильно a *= 5 операция сокращение
#

print(c)

# Логические операции

a = 1 > 4
print(a)# в выводе False так как не верно

a = 1 < 4 and 5 > 2
print(a)# в выводе True

a = 1  == 2#операция сравнения
print(a)

a = 1  != 2#операция неравенства
print(a)

a = 1 < 3 < 5
print(a)# можно использовать тройные неравенства

f = 1 > 2 or 4 < 6# дизюнкция когда одно из высказываний истина
print(f)

f = [1, 2, 3, 4]
print(f)
print(2 in f) # Tree так как 2 в этом массиве 
print(not 2 in f) # отрицание

is_odd = f[0] % 2 == 0 #проверяем остаток от делания на f с индексом 0 не равно 0
is_odd = not f[0] % 2 #более пайтеновский вариант записи
print(is_odd)


# Управляющие контструкции if, if-else

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

# Пример 2
username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же Маша!')
elif username == 'Марина':
    print('Я так Вас ждал, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ')
else:
    print('Привет, ', username)

# Управляющие контструкции while

#Оригинальное 23, 0 это инвертированное
#Пока не равно компануем перевернутое и делаем целочисленное деление на10

original = 23
inverted = 0
while original !=0:
    inverted = inverted*10 + (original % 10)
    original //= 10
print(inverted)

#или с else

original = 23
inverted = 0
while original !=0:
    inverted = inverted*10 + (original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('Хватит!)')
print(inverted)

# Управляющие конструкции for

for i in 1, 2, 3, 4, 5:
    print(i**2)

# Пример 2
list = [1, 2, 3, 4, 10, 5]
for i in list:
    print(list)

    # Пример 3
#r = range(10) # Выводит числа от 0 до 9
#for i in r:
##    print(i)
    # Пример 3
for i in range(1, 10, 2):# 2 дает тут прирощение 2 в интервале 1 до 10
    print(i)
    # Пример 4
for i in 'qwerty':
    print(i)

     #Немного о строках
# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) - получить количество символов
# print('ещё' in text) - проверить наличие подстроки в строке
# print(text.isdigit()) - проверить являются ли все числами 
# print(text.islower()) - проверить являются ли все нижнего регистра
# print(text.replace('ещё','ЕЩЁ')) - заменить слова и символы
# for c in text:
# print(c)

#Срезы

#text = 'съешь ещё этих мягких французских булок' 
#print(text[0]) # c (Обращение по индексу)
#print(text[1]) # ъ
#print(text[len(text)-1]) # к
#print(text[-5]) # б (с обратной стороны тика к это -1)
#print(text[:]) # print(text) 
#print(text[:2]) # съ 
#print(text[len(text)-2:]) # ок 
#print(text[2:9]) # ешь ещё 
#print(text[6:-18]) # ещё этих мягких 
#print(text[0:len(text):6]) # сеикакл 
#print(text[::6]) # сеикакл
#text = text[2:9] + text[-5] + text[:2] # ...


#Списки введение

numbers = [1, 2, 3, 4, 5]
print(numbers)
ran = range(1, 6)
print(type(ran)) #показывет тип
numbers = list(ran) #команда приведения тира ran  к типу list
print(type(numbers)) #показывет тип

print(numbers)                    # [1, 2, 3, 4, 5]
numbers[0] = 10     #присваемаем нулевому значение 10
print(f'{len(numbers)} len')   # получаем количество элементов воспользовавшись интерполяцией
print(numbers)                    # [10, 2, 3, 4, 5]
for i in numbers:
    i *=2   # в текущую переменную кладем НОВОЕ значение
    print(i)                      # [20, 4, 6, 8, 10]
print(numbers)                    # [10, 2, 3, 4, 5]

#Списки: введение
#colors = ['red', 'green', 'blue']

#for e in colors:
#      print(e) # red green blue 
#for e in colors:
#print(e*2) # redred greengreen blueblue

#colors.append('gray') # добавить в конец
#print(colors == ['red', 'green', 'blue', 'gray']) # True 
#colors.remove('red') #del colors[0] # удалить элемент

#Функции

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
arg = 1
print(f(arg))
print(type(f(arg)))