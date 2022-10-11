num=int(input())
d=0
sm=0
while num>9:
    sm=0
    while num!=0:
        d=num%10
        num=num//10
        d=pow(d,2)
        sm=sm+d
    num=sm
if(num==1 or num==7):
    print("True")
else:
    print("False")

