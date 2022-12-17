n=input()
l=list(map(int,input().split()))
c=[]
for i in l:
    for j in range(1,i+1,1):
        d=j*j
        if d==i:
            c.append(i)
print(sum(c))