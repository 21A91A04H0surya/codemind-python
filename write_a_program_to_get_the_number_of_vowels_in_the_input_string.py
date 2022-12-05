n=input()
c=0
v="aeiouAEIOU"
for i in n:
    if i in v:
        c+=1
if c>=1:
    print(c)
else:
    print(0)
    