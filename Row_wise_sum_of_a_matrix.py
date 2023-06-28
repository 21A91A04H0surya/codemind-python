r,c=map(int,input().split())
row=[0 for i in range(c)]
d=[row.copy() for i in range(r)]

k=[]
for i in range(r):
    v=list(map(int,input().split()))
    for j in range(c):
        d[i][j]=v[j]
for i in d:
    r=sum(i)
    k.append(r)
print(*k)