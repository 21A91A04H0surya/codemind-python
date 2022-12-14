n=input()
m=input()
l=list(n)
c=0
for i in l:
    if i==m:
        c+=1
if c==0:
    print("-1")
else:
    print(c)
