import random
n=0
a=0
b=0
count=0
while count<100000:
    n=random.choice([0, 1])
    if n==0:
        a+=1
    if n==1:
        b+=1
print(a, b)    
