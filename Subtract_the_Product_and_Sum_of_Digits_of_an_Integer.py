num=int(input())

m=1
n=0
while num%10:
    d=num%10
    num=num//10
    m=m*d
    n=n+d
    
print(m-n)

    