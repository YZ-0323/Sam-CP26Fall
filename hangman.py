import random

words = ["spooky", "halloween","pumpkin"]
#we can have multiple lists
#with various difficulty levels
target = random.choice(words)
print(target)

progress = ['_'] * len(target)

print(*progress)

attempts = 6
guessedletters = []

running = True

while running:

    guess = input("Enter a character: ")

    #validate guess (single character)

    guess = guess.lower().strip()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter!")
        continue

    if guess in guessedletters:
        print("You already guessed that letter!")
        continue
    guessedletters.append(guess)

    if guess not in target:
        print("Wrong guess!")
        #check if the user has lost the game
        attempts -= 1
        print("Attempts remaining:", attempts)
        if attempts == 0:
            print("Game over! The word was:", target)
            running = False

    else:
        for i in range(len(target)):
            if target[i] == guess:
                progress[i] = guess
        #check if the user has won the game
        if '_' not in progress:
            print("You win!")
            running = False

    print(*progress)
