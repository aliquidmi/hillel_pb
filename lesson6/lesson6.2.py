time = int(input("Enter seconds: "))

while time < 0 or time >= 8640000:
    print("Error time! Please enter true time: ")
    time = int(input("Enter seconds: "))

seconds = time % 60
minutes = (time // 60) % 60
hours = time // (60 * 60) % 24
days = time // (24 * 60 * 60)

days_words = {
    "singular": "день",
    "plural": "дні",
    "large": "днів",
}

if days % 10 == 1 and days % 100 != 11:
    day_word = days_words["singular"]
elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
    day_word = days_words["plural"]
else:
    day_word = days_words["large"]

print(f"{days} {day_word}, {hours:02}:{minutes:02}:{seconds:02}")
