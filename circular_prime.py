n=int(input())
ca=1
cb=1
x=str(n)
z=x[::-1]
y=int(z)
for i in range(2,n+1):
    if n%i==0:
        ca+=1
for j in range(2,y+1):
    if y%j==0:
        cb+=1
if ca==2 and cb==2:
    print("circular prime")
elif ca==2 or cb==2:
    print("prime but not a circular prime")
else:
    print("not prime")