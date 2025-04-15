import string

letters = string.ascii_letters

text = input("Enter two letters: ")
t = tuple(text)

start_letter = letters.index(t[0])
end_letter = letters.index(t[-1])

result = letters[start_letter:end_letter+1]
print(result)
