from collections import OrderedDict, namedtuple, defaultdict

Step = namedtuple("Step", ["input_number", "digits", "product"])
num = int(input("Enter number: "))

history = OrderedDict()

step = 1

while num > 9:
    n = tuple(int(i) for i in str(num))
    res = 1
    for i in n:
        res *= i

    history[step] = Step(num, n, res)
    num = res
    step += 1

count = defaultdict(int)
for step in history.values():
    count[step.product] += 1

print(num)
