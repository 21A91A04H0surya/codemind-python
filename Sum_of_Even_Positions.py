n=int(input())
s=0
lst=list(map(int,input().split()))
for i in range(len(lst)):
    if i%2==0:
        s=s+lst[i]
print(s)
    