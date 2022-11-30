import math
def prime(n):
    if n==1:
        return False
    sq=int(math.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
n=int(input())
l=[]
x=[]
c=0
for i in range(1,n):
    if n%i==0:
        l.append(i)
for i in l:
    if prime(i):
        c+=1
        x.append(i)
if c!=0:
    print(*x)
else:
    print("-1")