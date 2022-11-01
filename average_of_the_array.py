n=int(input())
lst=list(map(int,input().split()))
t=0
for i in range(len(lst)):
    t=t+lst[i]
av=t/n
format_av="{:.2f}".format(av)
print(format_av)