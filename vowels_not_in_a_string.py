n=input()
v="aeiou"
h=[]
l=[]
k=[]
for i in n:
    if i in v:
        h.append(i)
for j in v:
    if j in h:
        l.append(j)
    else:
        k.append(j)
if len(k)>0:
    print(*k)
else:
    print("0")