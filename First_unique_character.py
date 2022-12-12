s=input()
f=s.lower()
l=list(f)
for i in l:
    d=l.count(i)
    if d==1:
        print(i)
        break
else:
    print("-1")
