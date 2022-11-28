def pali(n):
    x=str(n)
    v=x[::-1]
    z=int(v)
    if z==n:
        return True
    return False
n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if pali(i):
        c.append(i)
print(len(c))