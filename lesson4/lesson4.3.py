import random

lst = [random.randint(0,9) for i in range(random.randint(3, 10))]
print(lst)
res = []
res.append(lst[0])
res.append(lst[2])
res.append(lst[-2])
print(res)
