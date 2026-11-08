a=[]
for i in range(5):
    a.append(int(input()))
b=int(input())
a.remove(min(a))
a.remove(max(a))
print(sum(a)*b)