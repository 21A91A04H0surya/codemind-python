n=int(input())
l=list(map(int,input().split()))
p=[]
for i in l:
    if i%2==0:
        p.append(i)
    else:
        break
print(sum(p))
    