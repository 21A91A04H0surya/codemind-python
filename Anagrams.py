a=input()
b=input()
if a==b:
    print("False")
x=a.upper()
y=b.upper()
c=set(x)
v=set(y)
if c==v:
    print("True")
else:
    print("False")