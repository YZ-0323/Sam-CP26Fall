s = input()

letters = ""
number = ""
action = ""

for c in s:
    if c.isupper():
        if number:
            print(letters, action, number)
            letters = ""
            number = ""
        letters += c
    elif c == "+":
        action = "tighten"
    elif c == "-":
        action = "loosen"
    elif c.isdigit():
        number += c

print(letters, action, number)