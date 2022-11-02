n=int(input())
l=[]
while n%10:
    d=n%10
    l.append(d)
    n=n//10
for i in range(len(l)):
    z=l.count(l[i])
    if z>=2:
        print("Not Unique Number")
        break
else:
    print("Unique Number")
        
        