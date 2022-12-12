a=input()
x=a.lower()
b=0
v=[]
k=[]
for i in x:
    v.append(i)
for i in v:
    if v.count(i)==1:
        k.append(i)
    else:
        break
if len(v)==len(k):
    print("True")
else:
    print("False")
    