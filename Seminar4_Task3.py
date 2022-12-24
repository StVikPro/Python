# Задача 3 Задать список из N элементов, заполненных числами из 
# [-N, N]. Найти произведение элементов на указанных позициях. 
# Число N вводится пользователем. Позиции хранятся в файле file.txt
# в одной строке одно число
# Изначально в файле до ввода N ничего нет.
# Позиции в файл вам нужно программно положить в зависимости от 
# выбранного N: если пользователь введет двойку, то в файле вряд 
# ли будут индексы 5 или 16.
# В решении должны быть и запись в файл, и чтение из файла.

from random import randint
def write_to_file(n):
    with open ('file_seminar4.txt', 'w') as file:
        for _ in range(n):
            file.write(f'{randint(-n,n)}')

write_to_file(5)