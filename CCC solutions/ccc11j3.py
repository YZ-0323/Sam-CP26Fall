a=[]
a.append(int(input()))
a.append(int(input()))
while(a[len(a)-1]<=a[len(a)-2]):
    a.append(a[len(a)-2]-a[len(a)-1])
print(len(a))
