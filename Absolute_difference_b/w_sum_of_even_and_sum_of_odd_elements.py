n=int(input())
sa=0
sb=0
lst=list(map(int,input().split()))
for i in range(len(lst)):
    if lst[i]%2==0:
        sa=sa+lst[i]
    else:
        sb=sb+lst[i]
print(abs(sa-sb))