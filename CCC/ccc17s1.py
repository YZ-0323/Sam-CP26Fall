n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

total_a = 0
total_b = 0
answer = 0

for i in range(n):
    total_a += a[i]
    total_b += b[i]

    if total_a == total_b:
        answer = i + 1

print(answer)