n = int(input())

for i in range(n):
    y, m, d = map(int, input().split())

    if (y, m, d) <= (1989, 2, 27):
        print("Yes")
    else:
        print("No")