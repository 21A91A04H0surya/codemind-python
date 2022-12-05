n=input()
l=n.split()
h=[]
w=[]
for i in range(len(l)-1,-1,-1):
    h.append(l[i])
for j in h:
    k=j[::-1]
    w.append(k)
print(*w)