n=input()
l=n.split()
for i in l:
    d=i
j=min(d)
if chr(ord(j)+32) in d:
    print(chr(ord(j)+32))
else:
    print(min(d))