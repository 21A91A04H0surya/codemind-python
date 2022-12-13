n=int(input())
l=list(map(int,input().split()))
x=set()
for i in l:
    x.add(i)
print(*x)