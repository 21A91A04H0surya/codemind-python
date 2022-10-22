# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
n=int(input())
s=0
num=n
while num%10:
    m=1
    d=num%10
    for i in range(1,d+1):
         m=m*i
    s=s+m
    num=num//10
    continue 
if s==n:
    print("The number %(n)d is a strong number"%{"n":n})
else:
    print("The number %(n)d is not a strong number"%{"n":n})

