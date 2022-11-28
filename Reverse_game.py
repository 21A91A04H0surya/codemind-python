n=int(input())
l=list(map(int,input().split()))
p=[]
for i in l:
    x=str(i)
    c=x[::-1]
    b=int(c)
    p.append(b)
print(*p)
    