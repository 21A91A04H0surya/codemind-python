n,m=map(int,input(). split ())
i=10
g=n%(i**m)
s=str(n)
f=s[::-1]
h=int(f)
b=h%(i**m)
r=str(b)
q=r[::-1]
t=int(q)
print(abs(g-t))
