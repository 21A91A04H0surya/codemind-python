n=int(input())
s=0
lst=list(map(int,input().split()))
a,b=map(int,input().split())
d=sum(lst)
for i in range(len(lst)):
    if lst[i]<a  or lst[i]>b:
        s=s+lst[i]
print(s)
