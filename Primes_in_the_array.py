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
l=list(map(int,input().split()))
c=[]
for i in l:
    if prime(i):
        c.append(i)
print(len(c))