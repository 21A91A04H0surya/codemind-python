def fib(n):
    a=0
    b=1
    s=0
    for i in range(1,n):
        a=b
        b=s
        s=a
        s=a+b
        if(s==n):
            return True
    return False
n=int(input())
if fib(n):
    print("True")
else:
    print("False")