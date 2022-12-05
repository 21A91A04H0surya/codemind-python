n=int(input())
l=list(map(int,input().split()))
for i in l:
    if i<0:
        i=-i
    i=str(i)
    i=list(i)
    print(len(i),end=' ')