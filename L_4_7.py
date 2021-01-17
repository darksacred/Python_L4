from math import factorial
from itertools import count

def fact(n):
    counter = 0
    for i in count(1):
        if counter >= n:
            break
        else:
            yield factorial(i)
            counter += 1

n = int(input(": "))

for el in fact(n):
    print(el)
