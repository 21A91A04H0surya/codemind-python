n=int(input())
l=list(map(int,input().split()))
k=int(input())
p=[]
for i in l:
    if i<=k:
        p.append(i)
    else:
        break
print(sum(p))
    