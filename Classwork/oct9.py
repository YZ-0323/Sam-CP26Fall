a = []
k=0
for i in range(int(input())):
    a.append(int(input()))
for i in range(int(len(a)/2)):
    if(a[i] == a[i+int(len(a)/2)]):
        k+=2
print(k)