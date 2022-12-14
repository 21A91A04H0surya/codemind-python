t=int(input())
for i in range(t):
    v=[]
    n=input()
    l=n.split()
    for i in l:
        k=i[::-1]
        if i==k:
            print("YES",end=" ")
            if len(k)%2==0:
                print("EVEN")
            else:
                print("ODD")
        else:
            print("NO")