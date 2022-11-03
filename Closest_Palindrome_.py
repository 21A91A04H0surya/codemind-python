n=int(input())
l=[]
la=[]
for i in range(n):
    num=str(i)
    z=num[::-1]
    y=int(z)
    if y==i:
        l.append(y)
for j in range(n+2,n*n):
    numa=str(j)
    a=numa[::-1]
    b=int(a)
    if b==j:
        la.append(b)
q=max(l)
w=min(la)
e=abs(q-n)
f=abs(w-n)
if f==e:
    print(q,w)
elif f>e:
    print(q)
else:
    print(w)


    
    


