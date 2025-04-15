import string

x = input("Enter string: ")

for c in string.punctuation:
    x = x.replace(c, "")
x = x[:140]
x = x.title()
res = "#" + x.replace(" ", "")
print(res)
