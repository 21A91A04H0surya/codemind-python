n=int(input())
lst=list(map(int,input().split()))
m=int(input())
for i in range(len(lst)):
    if lst[i]==m:
        print("True")
        break
else:
    print("False")