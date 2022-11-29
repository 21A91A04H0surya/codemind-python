n=int(input())
l=list(map(int,input().split()))
c=0
g=max(l)
for i in l:
    if g>=i:
        g=i
        c+=1
    else:
        print("no")
        break
if len(l)==c:
    print("yes")
    