import random

a = random.randint(1, 100)
g = 0
count = 0

print("Difficulty:")
print("1 = Easy (10 guesses)")
print("2 = Medium (7 guesses)")
print("3 = Hard (5 guesses)")

difficulty = int(input("Choose difficulty: "))

if difficulty == 1:
    k = 10
elif difficulty == 2:
    k = 7
else:
    k = 5

while g != a and count < k:
    g = int(input("Guess a number from 1 to 100: "))
    count += 1

    if g > a:
        print("Too high")
    elif g < a:
        print("Too low")

if g == a:
    print("You win! You took", count, "guesses.")
else:
    print("You lose! The number was", a)

#Features: difficulty levels, guess counter, guess limit, high/low hints