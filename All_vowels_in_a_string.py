n=input()
d=set()
v="aeiou"
for i in n:
    if i in v:
        d.add(i)
if len(d)==5:
    print("True")
else:
    print("False")
    