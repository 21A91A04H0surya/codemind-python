a,b=map(int,input().split())
l=list(map(int,input().split()))
x=list(map(int,input().split()))
a=[]
b=[]
c=0
for i in l:
    if i not in x and i not in a:
        c+=1
        a.append(i)
for j in x:
    if j not in l and j not in b:
        c+=1
        b.append(j)
        
print(c)