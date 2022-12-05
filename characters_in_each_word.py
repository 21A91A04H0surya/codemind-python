n=input()
c=0
h=[]
for i in n:
    if i==" ":
        h.append(c)
        c=0
        continue
    c+=1
h.append(c)
print(*h)