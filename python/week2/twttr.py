text = input("What is on your mind?")

for letter in text:
    if letter in ['a', 'e', 'i', 'o', 'u']:
        print(letter.replace(letter, ""), end="")
    else:
        print(letter, end="")
