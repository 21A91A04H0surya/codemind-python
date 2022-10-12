#reverse a number
num=int(input())
d=str(num)
while num>0:
    if(num>0):
        if(num%10!=0):
            print(d[::-1])
            break
        else:
            num=num//10
            x=str(num)
            print(x[::-1])
            break
else:
    w=abs(num)
    x=str(w)
    d=x[::-1]
    z=int(d)
    print(z*(-1))
