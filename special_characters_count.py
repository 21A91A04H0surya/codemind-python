n=input()
c=0
q="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
for i in n:
    if i not in q and i!=" ":
        c+=1
print(c)
    