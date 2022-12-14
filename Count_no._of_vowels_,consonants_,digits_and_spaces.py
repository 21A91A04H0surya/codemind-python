n=input()
l=list(n)
v="aeiou"
u="0123456789"
ov=0
co=0
di=0
sp=0
for i in l:
    if i in v:
        ov+=1
    elif i not in v and i not in u and i!=" ":
        co+=1
    elif i in u:
        di+=1
    elif i==" ":
        sp+=1
print("Vowels:",ov)
print("Consonants:",co)
print("Digits:",di)
print("White spaces:",sp)
    