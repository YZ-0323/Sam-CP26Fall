a = []

for i in range(int(input())):
    a.append(int(input()))

b = sorted(set(a), reverse=True)

bronze = b[2]

print(bronze, a.count(bronze))