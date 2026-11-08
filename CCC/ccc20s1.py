n = int(input())
a = []

for i in range(n):
    t, x = map(int, input().split())
    a.append((t, x))

a.sort()

ans = 0

for i in range(1, n):
    dt = a[i][0] - a[i-1][0]
    dx = abs(a[i][1] - a[i-1][1])

    v = dx / dt

    if v > ans:
        ans = v

print(ans)