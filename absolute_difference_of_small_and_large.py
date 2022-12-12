s=input()
l=s.split()
c=[]
for i in l:
    u=min(i)
    v=max(i)
    p=ord(u)
    q=ord(v)
    o=abs(p-q)
    c.append(o)
print(*c)
    
    