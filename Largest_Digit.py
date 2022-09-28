N=int(input())
sto=0
while(N):
    d=N%10
    if(d>sto):
        sto=d
    N=N//10
print(sto)
