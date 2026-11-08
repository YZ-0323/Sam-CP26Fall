a = []
n = []

while True:
    city, temp = input().split()
    n.append(city)
    a.append(int(temp))
    if city == "Waterloo":
        break
print(n[a.index(min(a))])