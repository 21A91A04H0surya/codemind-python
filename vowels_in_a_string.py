n=input()
m=input()
l=[]
c=0
for i in n:
    l.append(i)
for j in range(len(l)):
    if l[j]==m:
        c+=1
        v=j
        print("True")
        print(v)
        break
if c==0:
    print("False")

    