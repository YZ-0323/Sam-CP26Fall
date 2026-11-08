k = int(input())

icon = ["*x*", " xx", "* *"]

for row in icon:
    line = ""
    for ch in row:
        line += ch * k
    for i in range(k):
        print(line)
