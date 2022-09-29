n=int(input())
x=n
d=n*n
sum=0
while d:
    y=d%10
    sum=sum+y
    d=d//10
if(sum==x):
    print("Neon Number")
else:
    print("Not Neon Number")
