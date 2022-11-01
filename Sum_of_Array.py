n=int(input())
s=0
lst=list(map(int,input().split()))
for i in range(len(lst)):
    s=s+lst[i]
print(s)