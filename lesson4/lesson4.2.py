lst = [0, 1, 7, 2, 4, 8]
if len(lst) != 0:
    res = sum(lst[::2]) * lst[-1]
else:
    res = 0
print(res)
