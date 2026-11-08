import random


def ckdp(a):
    k = 0
    for i in range(len(a) - 1):
        for j in range(i, len(a) - 1):
            if a[i] == a[j + 1]:
                k = 1
                break
        if k == 1:
            break

    if k == 0:
        print("No duplicates found!")
    else:
        print("Duplicates found!")


ckdp([3, 7, 2, 7, 9])
ckdp([3, 7, 2, 5, 9])
ckdp([1, 1, 1, 1])
ckdp([5])



def ckmt(a, b):
    c = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            c += 1
    print(c)


ckmt([1, 2, 3, 4], [1, 5, 3, 8])
ckmt([4, 7, 2, 9], [4, 7, 2, 9])
ckmt([1, 2, 3, 4], [4, 3, 2, 1])
ckmt([5, 8, 2, 6], [5, 2, 8, 6])




def bnc(a, ans):
    c = 0
    for i in range(len(a)):
        if a[i] == ans[i]:
            c += 1

    print("Bulls =", c)

    k = 0
    for i in range(len(a)):
        if a[i] in ans and a[i] != ans[i]:
            k += 1

    print("Cows =", k)

    if c == 4:
        print("You win!")
        return True

    return False


ans = random.sample(range(10), 4)

while True:
    a = []

    print("Enter 4 different digits (0-9):")
    for i in range(4):
        a.append(int(input()))

    if len(set(a)) != 4 or any(x < 0 or x > 9 for x in a):
        print("Invalid guess! Try again.")
        continue

    if bnc(a, ans):
        break
