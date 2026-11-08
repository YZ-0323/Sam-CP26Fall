n = int(input())

highest = 0
winner = ""

for i in range(n):
    name = input()
    bid = int(input())

    if bid > highest:
        highest = bid
        winner = name

print(winner)