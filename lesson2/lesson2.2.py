x = int(input("Enter number: "))

x1 = x // 10000
x2 = (x // 1000) % 10
x3 = ((x // 100) % 100) % 10
x4 = (x % 100) // 10
x5 = x % 10

y = x5 * 10000 + x4 * 1000 + x3 * 100 + x2 * 10 + x1

print(y)
