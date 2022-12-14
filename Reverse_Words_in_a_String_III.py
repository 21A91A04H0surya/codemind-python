n=input()
l=n.split()
v=[]
for i in l:
    p=i[::-1]
    v.append(p)
print(*v)