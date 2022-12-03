n=int(input())
l=list(map(int,input().split()))
f=[]
for i in l:
    c=0
    while i%10:
        d=i%10
        c+=1
        i=i//10
    f.append(c)
g=min(f)
print(f.count(g))
        