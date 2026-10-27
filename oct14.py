a = [10, 20, 30, 40]
b = [90, 91, 92, 93]
c = []

for i in range(len(a)):
    c.append(a[i])
    c.append(b[i])

print(c)

# //-------------
a = [12, 45, 23, 67, 34]

a.sort()
print(a[-2])

# //-------------
a = [12, 45, 23, 67, 34]

largest = 0
second = 0

for i in a:
    if i > largest:
        second = largest
        largest = i
    elif i > second:
        second = i

print(second)

# //-------------
a = [10, 20, 30, 40]
b = []

for i in range(len(a) - 1, -1, -1):
    b.append(a[i])

print(b)