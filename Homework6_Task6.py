# 6 - Из списка выше оставьте только те пары, где сумма кортежа 
# кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

import random

numbers = [random.randint(1, 100) for _ in range(200)]
prod_list = enumerate(numbers)
print(f'Список пар, где сумма кратна 5 --> {list(filter(lambda x: (x[0]+x[1])%5==0, prod_list))}')