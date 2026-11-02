a = input()
b = input()
c = input()
d = input()
e = input()
f = input()
sum=0
if(a=="W"):
    sum+=1
if (b == "W"):
    sum += 1
if (c == "W"):
    sum += 1
if (d == "W"):
    sum += 1
if (e == "W"):
    sum += 1
if (f == "W"):
    sum += 1
if(sum>=5):
    print("1")
elif(sum>=3):
    print("2")
elif(sum>=1):
    print("3")
else:
    print("-1")