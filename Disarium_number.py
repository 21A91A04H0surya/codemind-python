n=int(input())
l=[]
p=[]
x=str(n)
z=x[::-1]
v=int(z)
while v%10:
    d=v%10
    l.append(d)
    v=v//10
for i in range(0,len(l)):
    f=0
    f=l[i]**(i+1)
    p.append(f)
if sum(p)==n:
    print("True")
else:
    print("False")

    

    