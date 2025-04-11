import keyword
import string

x = input("Enter string: ")

if x[0].isdigit() or x in keyword.kwlist or x.count('_') > 1 or ' ' in x:
    print(False)
elif any(c in string.punctuation for c in x if c != '_') or any(c.isupper() for c in x):
    print(False)
else:
    print(True)
