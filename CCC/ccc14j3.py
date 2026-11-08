aaa = 100
ddd = 100
for i in range(int(input())):
    a,b=[int(j) for j in input().split()]
    if a>b:
        ddd-=a
    elif a<b:
        aaa-=b
print(aaa)
print(ddd)