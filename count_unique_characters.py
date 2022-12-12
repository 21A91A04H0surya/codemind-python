s=input()
f=s.lower()
l=list(f)

c=set()
for i in l:
    if i==" ":
        continue
    
    elif(l.count(i)==1):
        c.add(i)
print(len(c))
        
