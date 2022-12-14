n=input()
l=list(n)
v=[]
w=[]
for i in l:
    d=l.count(i)
    v.append(d)
z=max(v)
for i in l:
    if l.count(i)!=z:
        w.append(i)
if len(w)>0:
    print(w[0])
else:
    print("-1")

   


