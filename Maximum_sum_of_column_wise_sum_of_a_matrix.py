r,c=map(int,input().split())
row=[0 for i in range(c)]
d=[row.copy() for i in range(r)]

k=[]
for i in range(r):
    v=list(map(int,input().split()))
    for j in range(c):
        d[i][j]=v[j]
for i in range(c):
    l=[]
    for j in range(r):
        l.append(d[j][i])
    k.append(sum(l))
print(max(k))