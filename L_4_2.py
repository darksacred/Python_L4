ls = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
ls_new = [el for i, el in enumerate(ls) if ls[i - 1] < ls[i]]

print(ls)
print(ls_new)