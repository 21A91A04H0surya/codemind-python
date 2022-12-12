s=input()
p=s.lower()
a=p.split()
c=0
for i in a:
    z=i[::-1]
    if z==i:
        c+=1
print(c)
    