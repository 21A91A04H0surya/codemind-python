t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    sto=0
    for i in range(a,b+1,1):
        d=a%10
        if(d==2 or d==3 or d==9):
            sto+=1
        a+=1
    print(sto)
            