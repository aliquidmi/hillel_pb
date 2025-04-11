import string

x = input("Enter string: ")

x = x.title()
for c in string.punctuation:
    x = x.replace(c, "")
x = x[:140]
res = "#" + x.replace(" ", "")
print(res)
print(len(res))
