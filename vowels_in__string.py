n=input()
l=list(n)
s=[]
v="aeiouAEIOU"
for i in l:
    if i==" ":
        continue
    if i in v:
        if i not in s:
            s.append(i)
if len(s)==0:
    print("-1")
else:
    print(*s)
        
        
    