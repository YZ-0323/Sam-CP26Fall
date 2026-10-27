a = []
total = 0
b = int(input())

for i in range(2*b):
    a.append(input())

for i in range(b):
    if a[i] == a[i+b]:
        total += 1

print(total)