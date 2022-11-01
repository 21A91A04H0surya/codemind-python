n=int(input())
lst=list(map(int,input().split()))
t=0
for i in range(len(lst)):
    t=t+lst[i]
av=t//n
for j in range(len(lst)):
    if av==lst[j]:
        print("True")
        break
else:
    print("False")