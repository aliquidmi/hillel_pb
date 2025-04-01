a = int(input("Enter a: "))
b = int(input("Enter b: "))
sym = input("Enter symbol: ")
if sym == "+":
    print("Result: ", a + b)
elif sym == "-":
    print("Result: ", a - b)
elif sym == "*":
    print("Result: ", a * b)
elif sym == "/":
    if b == 0:
        print("Error! b can`t be 0!")
    else:
        print("Result: ", a / b)
