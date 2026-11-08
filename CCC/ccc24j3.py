a = []
for i in range(int(input())):
    a.append(int(input()))

a.sort(reverse=True)



print(a[a.count(max(a))+a.count(a[a.count(max(a))])], a.count(a[a.count(max(a))+a.count(a[a.count(max(a))])]))
