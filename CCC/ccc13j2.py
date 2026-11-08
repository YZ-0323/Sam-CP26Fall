word = input()
valid = "IOSHZXN"

answer = "YES"

for letter in word:
    if letter not in valid:
        answer = "NO"

print(answer)