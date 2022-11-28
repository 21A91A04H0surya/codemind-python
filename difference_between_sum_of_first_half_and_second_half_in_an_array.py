n=int(input())
l=list(map(int,input().split()))
d=len(l)//2
s=0
sa=0
for i in range(0,d):
    s=s+l[i]
for j in range(d,len(l),1):
    sa=sa+l[j]
print(abs(s-sa))
