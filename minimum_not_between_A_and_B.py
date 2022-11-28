n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=[]
for i in l:
    if i<a or i>b:
        if i not in s:
            s.append(i)
if len(s)==0:
    print("-1")
print(min(s))            
            