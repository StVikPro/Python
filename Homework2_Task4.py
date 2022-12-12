# Задача 4 - По кругу стоят n человек. Ведущий посчитал m человек 
# по кругу, начиная с первого. При этом каждый из тех, кто 
# участвовал в этом счете, получил по одной монете, остальные 
# получили по две монеты. Далее человек, на котором остановился 
# счет, отдает все свои монеты следующему по счету человеку, а сам 
# выбывает из круга. Процесс продолжается с места остановки 
# аналогичным образом до последнего человека в круге. 
# Составьте алгоритм, который проводит эту игру. 
# Если хотите делать паузы, то импортируйте библиотеку time и 
# используйте оттуда функцию sleep. Определите номер этого 
# человека и количество монет, которые оказались у него в конце 
# игры.

# 4 - (если не получается, то альтернативная задача). 
# Составьте алгоритм нахождения случайного числа без использования 
# библиотеки random.
# https://habr.com/ru/company/vk/blog/574414/ - поможет вам эта статья.
# P.S. рекомендации по выполнению 4-го задания.
# 1. представьте список людей в виде списка индексов: [0,1,2,3,4...];
# 2. работайте одновременно со списком монет;
# 3. не надо писать сложных систем для "Процесс продолжается с 
# места остановки". Достаточно использовать срезы: переместите 
# оставшуюся часть списка вперед
# 4. после каждого выбывшего пусть работает input: хотите 
# продолжать или выйти из цикла игры?
# Остальное - это списки, циклы и условия, поэтому надеюсь, вы 
# справитесь;)

# Задание не смог сделать, очень сложно оказалось, списывать не стал
# планирую разобраться в будущем