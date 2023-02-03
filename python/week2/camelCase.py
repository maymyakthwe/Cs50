text = input("What's on your mind?")

for letter in text:
    if letter.isupper():
        print(letter.replace(letter, "_"+letter.lower()), end="")
    else:
        print(letter, end="")
