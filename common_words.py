s=input()
sa=input()
p=s.lower()
o=sa.lower()
l1=p.split()
l2=o.split()
b=[]
for i in l2:
    if i in l1:
        b.append(i)
print(*b)
        

