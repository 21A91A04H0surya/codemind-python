n=int(input())
l=list(map(int,input().split()))
d=len(l)//2
c=[]
v=[]
for i in range(d,len(l)):
    c.append(l[i])
c.reverse()
for i in range(d):
    c.append(l[i])
print(*c)