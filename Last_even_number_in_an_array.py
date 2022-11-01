n=int(input())
s=0
lst=list(map(int,input().split()))
for i in range(len(lst)):
    if lst[i]%2==0:
        s=lst[i]
print(s)