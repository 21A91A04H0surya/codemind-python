n=int(input())
for i in range(n):
    v=0
    m=input()
    b=list(m)
    f="0123456789"
    for j in b:
        if j in f:
            v+=1
    if v==0:
        print("No")
    else:
        print("Yes")
    