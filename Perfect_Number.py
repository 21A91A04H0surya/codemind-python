n=int(input())
i=1
t=0
while(i<n):
    x=n%i
    if(x==0):
        t=t+i
    i=i+1
if(t==n):
    print(True)
else:
    print(False)
