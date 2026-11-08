n = int(input())

s = 0
t = 0

for i in range(n):
    line = input().lower()
    s += line.count("s")
    t += line.count("t")

if t > s:
    print("English")
else:
    print("French")