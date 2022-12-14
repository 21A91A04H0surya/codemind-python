n=input()
l=list(n)
s=0
p="0123456789"
for i in l:
    if i in p:
        j=int(i)
        s=s+j
print(s)