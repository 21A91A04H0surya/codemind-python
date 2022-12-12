s=input()
l=s.split()
k=[]
p=[]
j=[]
h=[]
for i in l:
    d=min(i)
    k.append(d)
for i in l:
    o=max(i)
    p.append(o)
for i in k:
    f=ord(i)
    j.append(f)
a=sum(j)
for i in p:
    f=ord(i)
    h.append(f)
q=sum(h)
print(abs(a-q))
    