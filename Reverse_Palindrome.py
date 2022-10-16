num=int(input())
while True:
    a=str(num)
    s=a[::-1]
    d=int(s)
    sum=num+d
    f=str(sum)
    g=f[::-1]
    h=int(g)
    if sum==h:
        print(sum)
        break
    else:
        num=sum+h
        continue