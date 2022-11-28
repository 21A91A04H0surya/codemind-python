n=int(input())
l=list(map(int,input().split()))
d=sum(l)
if d%2==0:
    print("1")
else:
    print("0")