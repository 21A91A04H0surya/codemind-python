n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
j=[]
c=0
for i in l:
    if i>=a and i<=b:
        c+=1
        j.append(i)
if c==0:
    print("-1")
else:
    print(*j)
    