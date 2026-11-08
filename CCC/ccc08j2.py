b = 0
n = 0
a = ["A", "B", "C", "D", "E"]

while b != 4 or n != 1:
    b = int(input())
    n = int(input())

    if b == 1:
        for i in range(n):
            a.append(a.pop(0))
    elif b == 2:
        for i in range(n):
            a.insert(0, a.pop())
    elif b == 3:
        for i in range(n):
            a[0], a[1] = a[1], a[0]
    elif b == 4:
        print(*a)