def s(n):
    s=0
    while n:
        d=n%10
        s=s+d
        n=n//10
    return s
        
n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    c.append(s(i))
print(sum(c))