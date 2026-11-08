c = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total = 3 * (sum(a) + sum(b))

for i in range(c - 1):
    if a[i] == 1 and a[i + 1] == 1:
        total -= 2
    if b[i] == 1 and b[i + 1] == 1:
        total -= 2

for i in range(0, c, 2):
    if a[i] == 1 and b[i] == 1:
        total -= 2

print(total)
