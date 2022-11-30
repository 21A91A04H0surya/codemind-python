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
m=int(input())
l=[]
for i in range(n,m,1):
    if prime(i):
        l.append(i)
for j in l:
    print(j)