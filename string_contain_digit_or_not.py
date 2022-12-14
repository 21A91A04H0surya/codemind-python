n=input()
p=list(n)
c=0
a="0123456789"
for i in p:
    if i in a:
        c+=1
if c==0:
    print("Doesn't contain digit")
else:
    print("Contains",c,"digit")