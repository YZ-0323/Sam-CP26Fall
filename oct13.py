a=[60,3,70,14,59,33,12]
s=0
a.sort()
print(sum(a)/len(a))
a.remove(a[0])
a.remove(a[len(a)-1])
print(sum(a)/len(a))
