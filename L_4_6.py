from itertools import count
from itertools import cycle

ls = []
for el in count(3):
    if el > 10:
        break
    else:
        ls.append(el)
        print(el)

print(f'{5 * " "}')

counter = 0
for el in cycle(ls):
    if counter >= int(len(ls)):
        break
    print(el)
    counter += 1
