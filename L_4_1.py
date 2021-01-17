from sys import argv

name, time, stavka, bonus = argv
zp = int(time) * int(stavka) + int(bonus)
print(f'Зарплата сотрудника: {zp}')


