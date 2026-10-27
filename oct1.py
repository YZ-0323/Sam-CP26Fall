import random, time
a=time.time_ns()
n=random.randint(1,100)
while(a!=6):
    a=random.randint(1,100)
b=time.time_ns()
print(b-a)
