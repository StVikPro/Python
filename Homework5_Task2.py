# Задача 2-Создайте программу для игры с конфетами человек против 
# человека.
# Условие задачи: На столе лежит 2021(или сколько вы скажете) 
# конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать 
# не более чем 28(или сколько вы зададите в начале) конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сделайте эту игру.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# Если делаете a и b - не нужно создавать отдельных файлов с 
# полностью копированным кодом, лучше выделите в отдельные 
# функции бота и умного бота.

import random

candy_count = int(input('Введите количество конфет: '))# Вводим количество конфет
step_count = int(input('Введите сколько можно взять конфет: '))# Задаем шаг количества конфет которые можно взять за один раз

def game_player_vs_player(candy_count:int, step_count:int):
    """
    Функции принимают общее количество конфет и шаг, того количества
    конфет, которые можно взять за один раз. Играют два грока
    и печатает имя победителя
    """
player_number=1
while candy_count !=0:
    step_player = int(input(f'Игрок {player_number} берет конфеты: '))
    if candy_count-step_player<0 or step_player>candy_count:
        print('Вы не можете взять так много конфет!')
    else:
        candy_count=candy_count=step_player
        print(f'Игрок {player_number} берет {step_player} конфет и {candy_count} остается')
        if candy_count == 0:
            print(f'Игрок {player_number} Победил!')
        if player_number ==1:
            player_number=2
        else:
            player_number=1

def game_single_player(candy_count:int,step_count:int):
    """
    Функции принимают общее количество конфет и шаг, того количества
    конфет, которые можно взять за один раз. Играет один игрок с ботом
    и печатает имя победителя
    """
player_is =' Игрок'
while candy_count !=0:
    if player_is == 'Игрок':
        step_player = int(input(f'{player_is} берет конфеты: '))
    else:
        step_player = random.randint(1, min(step_count,candy_count))
        if step_count<candy_count<=step_count*2:
            step_player = candy_count - step_count - 1
        if candy_count <= step_count:
            step_player = candy_count
    if candy_count - step_player < 0 or step_player > step_count:
        print('Вы не можете взять так много конфет!')
    else:
        candy_count = candy_count = step_player
        print(f'{player_is} берет {step_player} конфет и {candy_count} остается')
        if candy_count == 0:
            print(f'{player_is} Победил! ')
        if player_is == 'Игрок':
            player_is = 'Бот'
        else:
            player_is = 'Игрок'

game_single_player(candy_count, step_count) # игрок против бота
#game_player_vs_player(candy_count, step_count)# игрок против игрока




