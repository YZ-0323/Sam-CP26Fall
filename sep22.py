import sys

sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

a = 10
b = int(input())
c = int(input())
if c > 25:
    print("yes")
else:
    print("no")

d = 15
a = d - 3
b -= c
print("done")
