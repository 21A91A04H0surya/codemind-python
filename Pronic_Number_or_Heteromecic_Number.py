x=int(input())
i=0
d=1
for i in range(x):
    w=d
    d+=1
    if(x==w*i):
        print("YES")
        break
else:
    print("NO")