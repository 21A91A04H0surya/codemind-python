a=input()
b=input()
p=a.lower()
o=b.lower()
l1=[]
l2=[]
m=set()
for i in p:
    if i==" ":
        continue
    l1.append(i)
for i in o:
    if i==" ":
        continue
    l2.append(i)
for i in l1:
    if i in l2:
        m.add(i)
m=list(m)
m.sort()
if len(m)==0:
    print("-1")
else:
    for i in m:
        print(i,end="")
        
    