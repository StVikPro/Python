# Задача 1-Напишите программу, удаляющую из текста все слова, 
# содержащие заданную строку.
# Пример:
# Пугать ты галок пугай => заданная строка "галок" => Пугать ты пугай
# Пугать ты галок пугай => заданная строка "пуг" => Пугать ты галок

string = input('Введите строку для фильтрации: \n')
word = input('Введите слово, необходимое для удаления: \n')

split_str = string.split()
filtered_str = ' '.join(filter(lambda n: word not in n, split_str))

print('Строка после фильтрации: ', filtered_str)
