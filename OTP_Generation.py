n=input()
k=list(n)
p=[]
m=[]
for i in k:
    f=int(i)
    p.append(f)
    


for i in p:
    if i%2!=0:
        j=i*i
        m.append(j)
for i in m :
    print(i,end="")