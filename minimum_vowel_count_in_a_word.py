n=input()
l=list(n)
c=0
f=0
v="aeiou"
k=[]
p=0
for i in l:
    if i==" ":
        k.append(c)
        c=0
        continue
    if i in v:
        c+=1
k.append(c)
print(min(k))
        
    