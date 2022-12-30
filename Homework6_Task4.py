# Задача 4 - Дан список URL различных сайтов. Нужно составить 
# список доменных имен сайтов.

urls_list = ['https://dzen.ru/?yredirect=true',
             'https://www.google.ru',
             'https://www.apple.com/ru/',
             'https://www.avito.ru',
             'https://kotlinlang.org']

domens_list = []
for i in range(len(urls_list)):
    change = urls_list[i].partition('//')[-1]
    change = change.partition('/')[0]
    domens_list.append(change)

print(*domens_list,sep = " \n ")