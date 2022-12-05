n=input()
l=n.split()
h=[]
for i in range(len(l)):
    if i%2==0:
        j=l[i]
        g=j[::-1]
        h.append(g)
    else:
        h.append(l[i])
print(*h)
    