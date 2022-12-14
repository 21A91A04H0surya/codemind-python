n=input()
l=list(n)
v="0123456789"
p=[]
s=0
for i in l:
    if i in v:
        j=int(i)
        p.append(j)
print(sum(p))        