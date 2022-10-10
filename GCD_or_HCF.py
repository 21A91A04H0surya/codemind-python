a,b=map(int,input().split())
res=1
t=2
while True:
    if(a%t==0 and b%t==0):
        res=res*t
        a=a//t
        b=b//t
    else:
        t=t+1
    if(a<t or b<t):
      print(res)
      break