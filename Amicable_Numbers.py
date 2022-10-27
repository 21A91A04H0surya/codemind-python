# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
n=int(input())
m=int(input())
sa=0
sb=0
for i in range (1,n):
    if n%i==0:
        sa+=i
for j in range (1,m):
    if m%j==0:
         sb+=j
        
if sa==m and sb==n:
    print("Amicable")
else:
    print("Not Amicable")
