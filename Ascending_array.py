n=int(input())
l=list(map(int,input().split()))
g=0
c=0
for i in l:
    if i>g:
        g=i
        c+=1
    else:
        print("no")
        break
if c==len(l):
    print("yes")