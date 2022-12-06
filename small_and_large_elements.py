n=input()
l=n.split()
h=[]
h.append(min(l[0]))
h.append(max(l[-1]))
print(*h)