a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
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
