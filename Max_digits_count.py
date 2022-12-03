n=int(input())
l=list(map(int,input().split()))
g=[]
for i in l:
    c=0
    while i%10:
        d=i%10
        c+=1
        i=i//10
    g.append(c)
h=max(g)
print(g.count(h))