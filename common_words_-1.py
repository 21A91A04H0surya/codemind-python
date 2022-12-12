s1=input()
s2=input()
s3=s1.lower()
s4=s2.lower()
l1=s3.split()
l2=s4.split()
c=0
for i in l1:
    if i in l2:
        c+=1
print(c)