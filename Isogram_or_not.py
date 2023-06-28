n=input()
p=list(n)
l=0
for i in p:
    if p.count(i)!=1:
        print("False")
        l+=1
        break
    
        
if l==0:
    
    print("True")