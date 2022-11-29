n,m=map(int,input().split())
l=list(map(int,input().split()))
x=list(map(int,input().split()))
c=[]
for i in l:
    if i in x:
        if i not in c:
            c.append(i)
        
print(*c)
    
