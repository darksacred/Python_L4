from functools import reduce

def sum_reduce(prev_el, el):
    return prev_el + el

# Тут почемуто добавляется в конце None, пока не понял почему.
#print(f'{print(reduce(sum_reduce,[el for el in range(100, 1000) if el % 2 == 0]))}')

lss = [el for el in range(100, 1002) if el % 2 == 0]
print(f'Сумма чисел от 100 до 1000, кратные 2: {reduce(sum_reduce, lss)}')

