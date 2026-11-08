import random
def coin():
    x=random.randint(1,2)
    if x==1:
        print("Heads")
    else:
        print("Tails")
def die():
    x = random.randint(1, 6)
    if x == 1:
        print("1")
    elif x==2:
        print("2")
    elif x==3:
        print("3")
    elif x==4:
        print("4")
    elif x==5:
        print("5")
    else:
        print("6")
def guess():
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
def sub(n):
    while n > 0:
        print("Stones left:", n)
        player = int(input("Take 1~3 stones: "))
        if player not in [1,2,3] or player > n:
            print("Invalid move!")
            continue
        n -= player
        if n == 0:
            print("You win!")
            return
        bot = n % 3
        if bot == 0:
            bot = 1
        n -= bot
        print("Bot takes", bot, "stones")
        if n == 0:
            print("Bot wins!")
            return
while True:
    print("1.Flip Coin")
    print("2.Throw Die")
    print("3.Guess Number")
    print("4.Subtraction Game")
    print("0.Exit")
    choice=int(input("Enter your choice:"))
    if choice==0:
        break
    elif choice==1:
        coin()
    elif choice==3:
        guess()
    elif choice==4:
        sub(15)
    else:
        die()
print("Thank you")