n=input()
l=n.split()
h=[]
for i in range(len(l)):
    d=min(l[i])
    f=max(l[i])
    h.append(d)
    h.append(f)
print(*h)
    