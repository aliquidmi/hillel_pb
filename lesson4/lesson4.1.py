lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
index = 0
for l in lst:
    if l != 0:
        lst[index] = l
        index += 1
for i in range(index, len(lst)):
    lst[i] = 0
print(lst)
