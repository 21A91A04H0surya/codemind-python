a=input()
b=input()
z=a.lower()
x=b.lower()
l1=z.split()
l2=x.split()
c=0
for i in l1:
    if i in l2 and l1.count(i)==1 and l2.count(i)==1:
        c+=1
print(c)
    