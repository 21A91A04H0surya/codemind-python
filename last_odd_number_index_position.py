n=int(input())
s=0
lst=list(map(int,input().split()))
for i in range(len(lst)):
    if lst[i]!=0:
        s=i
print(s)